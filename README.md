# Superticket.sk – nový web

Statický web (HTML + CSS + malý JS, bez knižníc a bez jQuery). Predaj vstupeniek zostáva v **Bzuco** – napojený rovnako ako na súčasnom webe.

## Čo je v balíku

```
web/      ← toto nahrajte na hosting (koreň domény superticket.sk)
zdroj/    ← zdroj na úpravy: data.py (podujatia, novinky, minulé akcie, FAQ), legal.py (VOP, GDPR), templates/, site_src/
```

Po úprave textov v `zdroj/data.py` alebo `zdroj/legal.py` spustite `python3 build.py` (treba `pip install jinja2`) – nový web sa vytvorí v `dist/deploy`.

## Adresy (zostávajú rovnaké ako dnes)

| Stránka | URL |
|---|---|
| Úvod | `/` |
| BIG SUMMER FEST 2027 | `/big-summer-fest-2027` |
| GIMS | `/gims` |
| Tvoja 90's Show Košice | `/tvoja90kosice` |
| 30 rokov LUNETIC | `/30-rokov-lunetic` (nová) |
| Vstupenky a košík (Bzuco) | `/vstupenky` |
| Minulé akcie | `/minule-akcie` |
| Časté otázky | `/caste-otazky` |
| Kontakt | `/kontakt` |
| Obchodné podmienky | `/obchodne-podmienky` |
| Ochrana osobných údajov | `/ochrana-osobnych-udajov` |

Každá stránka je priečinok s `index.html`, takže funguje na Cloudflare Pages, Netlify aj bežnom Apache/Nginx hostingu. Staré `/akcie`, `/sutaz`, `/pravidla` sa presmerujú (`_redirects` pre Cloudflare/Netlify, `.htaccess` pre Apache).

## Bzuco – ako je to zapojené

Súčasný web (Pagebuilder) používa Bzuco inštanciu **tvoja-show.bzuco.cloud**. Nový web používa ten istý skript a rovnakú konfiguráciu:

```html
<script>
var bzucoConfig = {
  headless: false, paymentBackToShopLink: "/vstupenky/", singleAuto: true, vat: false,
  floatingBasket: true, animation: 'fade', language: "sk",
  callbackAddToBasket: function () { stToast(); },          // vlastné upozornenie „Vstupenky sú v košíku“
  onReady: function (api) { bzucoApi = api; }
};
bzucoConfig.detail = 244;   // GIMS
</script>
<div class="bzuco"><script src="https://tvoja-show.bzuco.cloud/resources/frontend/embed.js"></script></div>
```

| Podujatie | Bzuco | Spôsob |
|---|---|---|
| BIG SUMMER FEST 2027 | event 247 | headless + tlačidlá `bzuco-widget-add-to-basket` (bloky 1148 = 3-dňová 99,90 €, 1150 = PREMIUM 179,90 €, 1149 = VIP 399,90 €) |
| GIMS | event 244 | `bzucoConfig.detail = 244` |
| Tvoja 90's Show Košice | event 245 | `listFilter` [245] + `singleAuto` (rovnako ako dnes) |
| 30 rokov LUNETIC | **chýba ID** | doplniť v `data.py` → `"bzuco": {"detail": ID}` |

- Košík v hlavičke je Bzuco widget `bzuco-widget-basket` → `/vstupenky/#/kosik`.
- Rozdiel oproti dnešku: `useWebJquery` je vypnuté (nový web nemá jQuery, Bzuco si načíta vlastné).
- Ak sa Bzuco do 12 s nenačíta, stránka ukáže náhradnú správu s e-mailom podpory.
- Bzuco používa cookie `bzuco-token` (košík) – podľa dokumentácie Bzuco ju treba uviesť medzi nutnými cookies.
- Dokumentácia: https://tvoje-show.bzuco.cloud/resources/docs/ , tester konfigurácie: https://tvoje-show.bzuco.cloud/resources/config/

### Pred prepnutím domény otestujte
1. Nahrajte `web/` na testovaciu adresu (napr. Cloudflare Pages `*.pages.dev`).
2. Skúste nákup na všetkých podujatiach až po platobnú bránu. Ak Bzuco na inej doméne nenačíta predaj, požiadajte Bzuco o povolenie testovacej domény – na superticket.sk to bude fungovať ako dnes.
3. Overte, že návrat z platby končí na `/vstupenky/`.

## Meranie a cookies
Google Tag Manager `GTM-PH7LK2BZ` (dnes cez neho beží GA4 aj Meta Pixel) sa načíta až po kliknutí na „Povoliť všetky“ a iba na doméne superticket.sk.

## Na doplnenie / overenie
- **Lunetic**: Bzuco ID, čas začiatku a text o podujatí.
- **Minulé akcie**: bannery sú v `img/minule/` (1100 × 413 px + zmenšenina `-sm`). Novú akciu pridáte do `PAST` v `data.py`.
- **Cookies v Ochrane osobných údajov**: zoznam je prevzatý zo súčasného webu (cookies Pagebuildera `nette-browser`, `PHPSESSID`, `PB_CookiesConsent`). Na novom webe ich nahradí `bzuco-token`; doplniť treba aj `_fbp` (Meta Pixel).
- **Právne texty**: prevzaté zo superticket.sk s drobnými jazykovými opravami (napr. „ním zvolené“, nariadenie EÚ 2016/679 namiesto chybného 2017/679). Obsah nemenený.
- **Hodiny podpory**: FAQ uvádza e-mail Po – Pi 09:00 – 16:00, kontakt uvádza telefón Po – Pi 09:00 – 15:00 – ponechané obe.
- **Cenová vlna / odpočty**: Tvoja 90's má koniec 2. cenovej vlny 15. 10. 2026 o 23:59 (`wave` v `data.py`). GIMS má pole `wave` pripravené – doplňte dátum konca vlny a pás s odpočtom sa zobrazí sám. Po uplynutí sa pás skryje.
- **Referencie**: logá sú v `img/ref/`, zoznam v `REFS` v `data.py`.
- **Novinky**: všetky 4 majú zatiaľ dátum 28. 9. 2026 – upravte na skutočné dátumy oznámení v `data.py`.
- **Odznak nad pätičkou**: čísla (5+ rokov, 150 000+ zákazníkov, 3 krajiny, 250+ podujatí) sú v `STATS` v `data.py`.
- **BSF**: texty v časti „Tretí ročník“ sú prepísané do vykania (namiesto „čaká ťa… poznáš“).
- **BSF bloky 1150/1149**: priradenie PREMIUM/VIP je podľa poradia na súčasnom webe – overte pri teste.
