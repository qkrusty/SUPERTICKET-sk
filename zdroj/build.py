# -*- coding: utf-8 -*-
"""Generátor statického webu superticket.sk.
   python3 build.py  ->  dist/deploy (na hosting)  +  dist/preview (náhľad v artefakte)
"""
import json, os, shutil, hashlib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
import data, legal

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'site_src')

# slug -> (šablóna, titulok, popis)
PAGES = {
    'minule-akcie': 'Minulé akcie',
    'caste-otazky': 'Časté otázky',
    'kontakt': 'Kontakt',
    'obchodne-podmienky': 'Obchodné podmienky',
    'ochrana-osobnych-udajov': 'Ochrana osobných údajov',
    'vstupenky': 'Vstupenky',
}
TAG_LABELS = {'novinka': 'Novinka', 'zmena': 'Zmena', 'info': 'Info'}


def asset_version():
    h = hashlib.md5()
    for f in ('assets/site.css', 'assets/site.js'):
        h.update(open(os.path.join(SRC, f), 'rb').read())
    return h.hexdigest()[:8]


def make_env():
    env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')),
                      autoescape=select_autoescape(['html']), trim_blocks=True, lstrip_blocks=True)
    return env


def bzuco_config(e):
    """Inline konfigurácia Bzuco – rovnaká ako na súčasnom webe (bez useWebJquery, nový web nemá jQuery)."""
    bz = e['bzuco']
    if not bz:
        return ''
    lines = [
        "var bzucoApi;",
        "var bzucoConfig = {",
        f"  headless: {'true' if bz.get('headless') else 'false'},",
        '  paymentBackToShopLink: "/vstupenky/",',
        "  singleAuto: true,",
        "  vat: false,",
        "  floatingBasket: true,",
        "  animation: 'fade',",
        '  language: "sk",',
        "  callbackAddToBasket: function () { if (window.stToast) window.stToast(); },",
        "  onReady: function (api) { bzucoApi = api; document.documentElement.classList.add('bz-ready'); }",
        "};",
    ]
    if bz.get('detail'):
        lines.append(f"bzucoConfig.detail = {bz['detail']};")
    if bz.get('list'):
        ids = ', '.join(str(x) for x in bz['list'])
        lines.append("bzucoConfig.listFilter = function (item) { return [" + ids + "].indexOf(item.id) !== -1; };")
    return Markup("<script>\n" + "\n".join(lines) + "\n</script>")


def shop_config():
    return Markup("<script>\nvar bzucoApi;\nvar bzucoConfig = {\n  headless: false,\n  paymentBackToShopLink: \"/vstupenky/\",\n  singleAuto: true,\n  vat: false,\n  floatingBasket: false,\n  animation: 'fade',\n  language: \"sk\",\n  onReady: function (api) { bzucoApi = api; document.documentElement.classList.add('bz-ready'); }\n};\n</script>")


def event_jsonld(e):
    d = {
        "@context": "https://schema.org",
        "@type": "Festival" if e['key'] == 'bsf' else "MusicEvent",
        "name": e['name'],
        "startDate": e['iso_start'],
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "location": {"@type": "Place", "name": e['venue'],
                     "address": {"@type": "PostalAddress", "addressLocality": e['city'], "addressCountry": "SK"}},
        "image": [data.SITE['domain'] + '/' + e['og']],
        "description": e['summary'],
        "organizer": {"@type": "Organization", "name": data.CONTACT['company'], "url": data.SITE['domain']},
        "offers": {"@type": "Offer", "url": f"{data.SITE['domain']}/{e['slug']}/", "priceCurrency": "EUR",
                   "availability": "https://schema.org/InStock"},
    }
    if e.get('iso_end'):
        d['endDate'] = e['iso_end']
    if e['stub_value'].endswith('€'):
        d['offers']['price'] = e['stub_value'].replace(' €', '').replace(',', '.')
    if e['chips'] and e['key'] != 'gims':
        d['performer'] = [{"@type": "MusicGroup", "name": c} for c in e['chips']]
    return json.dumps(d, ensure_ascii=False)


def build(mode):
    out = os.path.join(ROOT, 'dist', mode)
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    shutil.copytree(os.path.join(SRC, 'img'), os.path.join(out, 'img'))
    shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(out, 'assets'))

    env = make_env()
    ver = asset_version()

    def u(key):
        if mode == 'deploy':
            return '/' if key == 'home' else f'/{key}/'
        return 'index.html' if key == 'home' else f'{key}.html'

    def a(path):
        return ('/' + path) if mode == 'deploy' else path

    common = dict(mode=mode, u=u, a=a, ver=ver, site=data.SITE, contact=data.CONTACT, events=data.EVENTS,
                  ev_by_key={e['key']: e for e in data.EVENTS}, tag_labels=TAG_LABELS, stats=data.STATS, webs=data.WEBS, refs=data.REFS, social=data.SOCIAL,
                  months=['', 'jan', 'feb', 'mar', 'apr', 'máj', 'jún', 'júl', 'aug', 'sep', 'okt', 'nov', 'dec'])

    def page(tpl, key, title, description, og_image='img/og-superticket.jpg', head_extra='', jsonld='',
             preload=(), fragment=False, body_class='', **ctx):
        main = Markup(env.get_template(tpl).render(**common, page=key, **ctx))
        html = env.get_template('base.html').render(
            **common, page=key, title=title, description=description, og_image=og_image,
            canonical=u(key) if mode == 'deploy' else '', main=main, scripts='', head_extra=Markup(head_extra),
            jsonld=jsonld, preload=list(preload), fragment=fragment, body_class=body_class, og_title=None)
        if mode == 'deploy':
            path = os.path.join(out, 'index.html') if key == 'home' else os.path.join(out, key, 'index.html')
            if key == '404':
                path = os.path.join(out, '404.html')
        else:
            path = os.path.join(out, 'index.html' if key == 'home' else f'{key}.html')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    # Úvod
    home_ld = json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "Superticket",
                          "legalName": data.CONTACT['company'], "url": data.SITE['domain'],
                          "logo": data.SITE['domain'] + "/img/apple-touch-icon.png",
                          "email": data.CONTACT['support'], "sameAs": [data.SITE['facebook'], data.SITE['instagram']]},
                         ensure_ascii=False)
    page('index.html', 'home',
         'Superticket nový web' if mode == 'preview' else 'Superticket – vstupenky na BIG SUMMER FEST, GIMS, Tvoja 90\'s Show a Lunetic',
         'Oficiálny predaj vstupeniek na BIG SUMMER FEST 2027, GIMS, Tvoja 90\'s & Millenium Show a 30 rokov LUNETIC. Bezpečná platba kartou, vstupenky e-mailom.',
         jsonld=home_ld if mode == 'deploy' else '', preload=[data.EVENTS[0]['tile_img']],
         fragment=(mode == 'preview'), news=data.NEWS)

    # Podujatia
    for e in data.EVENTS:
        head = bzuco_config(e) if mode == 'deploy' else ''
        title = f"{e['name']} – vstupenky | {e['date']}, {e['venue']} {e['city']}"
        desc = f"Vstupenky na {e['name']}: {e['date_long']}, {e['venue']}, {e['city']}. {e['summary']}"
        page('event.html', e['slug'], title, desc, og_image=e['og'], head_extra=head, body_class='is-event',
             jsonld=event_jsonld(e) if mode == 'deploy' else '', preload=[e['hero_img']], e=e)

    # Podstránky
    page('vstupenky.html', 'vstupenky', 'Vstupenky a košík | Superticket',
         'Predaj vstupeniek na podujatia Superticket – vyberte podujatie, pridajte vstupenky do košíka a zaplaťte online.',
         head_extra=shop_config() if mode == 'deploy' else '')
    page('past.html', 'minule-akcie', 'Minulé akcie | Superticket',
         'Podujatia, ktoré sme už zorganizovali – BIG SUMMER FEST, Tvoja 90\'s Show, Kabát, Killer Queen, ABBA Mania a ďalšie.',
         past=data.PAST)
    page('faq.html', 'caste-otazky', 'Časté otázky | Superticket',
         'Odpovede na časté otázky o nákupe vstupeniek, platbe, doručení, výmene a zrušení podujatia.', faq=data.FAQ)
    page('kontakt.html', 'kontakt', 'Kontakt | Superticket',
         f"Zákaznícka podpora Superticket: {data.CONTACT['support']}, tel. {data.CONTACT['phone']} ({data.CONTACT['phone_hours']}).")
    vop_arts = [(i_, t, h.replace('{kontakt}', u('kontakt'))) for i_, t, h in legal.VOP]
    # (legal stránky renderujeme zvlášť, lebo šablóna používa vlastné „title“)
    for key, h1, lead, intro, arts, sign, cookies, label, desc in [
        ('obchodne-podmienky', 'Obchodné podmienky', 'Obchodné podmienky pre predaj vstupeniek a reklamačný poriadok.',
         legal.VOP_INTRO, vop_arts, legal.VOP_SIGN, '', 'Článok',
         'Obchodné podmienky pre predaj vstupeniek SUPERTICKET, s.r.o. vrátane reklamačného poriadku.'),
        ('ochrana-osobnych-udajov', 'Ochrana osobných údajov', legal.GDPR_INTRO, '', legal.GDPR, legal.GDPR_SIGN,
         legal.COOKIES, 'Bod', 'Ako SUPERTICKET, s.r.o. spracúva osobné údaje kupujúcich a aké cookies používa web superticket.sk.'),
    ]:
        main = Markup(env.get_template('legal.html').render(**common, page=key, title=h1, lead=lead, intro=intro,
                                                           arts=arts, sign=sign, cookies=cookies, label=label))
        html = env.get_template('base.html').render(
            **common, page=key, title=f'{h1} | Superticket', description=desc, og_image='img/og-superticket.jpg',
            canonical=u(key) if mode == 'deploy' else '', main=main, scripts='', head_extra='', jsonld='',
            preload=[], fragment=False, body_class='', og_title=None)
        path = os.path.join(out, key, 'index.html') if mode == 'deploy' else os.path.join(out, f'{key}.html')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(html)

    if mode == 'deploy':
        page('404.html', '404', 'Stránka neexistuje | Superticket', 'Stránka neexistuje.')
        write_deploy_extras(out)
    return out


def write_deploy_extras(out):
    dom = data.SITE['domain']
    urls = ['/'] + [f"/{e['slug']}/" for e in data.EVENTS] + [f'/{k}/' for k in PAGES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{dom}{p}</loc></url>' for p in urls]
    sm.append('</urlset>')
    open(os.path.join(out, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
    open(os.path.join(out, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {dom}/sitemap.xml\n')
    # Cloudflare Pages / Netlify – presmerovania starých adries z Pagebuildera
    open(os.path.join(out, '_redirects'), 'w').write(
        "/akcie        /#podujatia   301\n"
        "/sutaz        /             302\n"
        "/pravidla     /             302\n"
        "/home         /             301\n")
    open(os.path.join(out, '_headers'), 'w').write(
        "/img/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "/assets/*\n  Cache-Control: public, max-age=604800\n"
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    # Apache (napr. Websupport) – ekvivalent _redirects
    open(os.path.join(out, '.htaccess'), 'w').write(
        "ErrorDocument 404 /404.html\n"
        "RewriteEngine On\n"
        "RewriteRule ^akcie/?$ /#podujatia [R=301,NE,L]\n"
        "RewriteRule ^(sutaz|pravidla)/?$ / [R=302,L]\n"
        "<IfModule mod_expires.c>\n  ExpiresActive On\n  ExpiresByType image/webp \"access plus 1 year\"\n"
        "  ExpiresByType image/png \"access plus 1 year\"\n  ExpiresByType image/jpeg \"access plus 1 year\"\n"
        "  ExpiresByType text/css \"access plus 1 week\"\n  ExpiresByType application/javascript \"access plus 1 week\"\n</IfModule>\n")


if __name__ == '__main__':
    for m in ('deploy', 'preview'):
        print('built', build(m))
