# -*- coding: utf-8 -*-
"""Obsah webu superticket.sk – upravujte tu, potom spustite build.py."""

SITE = {
    "name": "Superticket",
    "domain": "https://www.superticket.sk",
    "claim": "Oficiálny predaj vstupeniek na podujatia agentúry tvojaSHOW.sk.",
    "facebook": "https://www.facebook.com/superticket.sk",
    "instagram": "https://www.instagram.com/superticket.sk/",
    # Bzuco – rovnaká inštancia ako na súčasnom webe
    "bzuco_embed": "https://tvoja-show.bzuco.cloud/resources/frontend/embed.js",
    # Meranie – načíta sa až po súhlase s cookies a iba na doméne superticket.sk
    # (GA4 G-YXS5K4YE12 a Meta Pixel 390267056683160 sa dnes načítavajú cez tento GTM kontajner)
    "gtm": "GTM-PH7LK2BZ",
    "bsf_web": "https://bigsummerfest.sk/",
}

CONTACT = {
    "support": "podpora@superticket.sk",
    "support_hours": "Po – Pi 09:00 – 16:00",
    "info": "info@superticket.sk",
    "marketing": "marketing@tvojashow.sk",
    "phone": "+421 918 967 940",
    "phone_href": "+421918967940",
    "phone_hours": "Po – Pi 09:00 – 15:00",
    "company": "SUPERTICKET, s.r.o.",
    "street": "Holečkova 789/49",
    "city": "Smíchov, 150 00 Praha 5",
    "ico": "17555710",
    "register": "OR v Praze, spisová značka C 373064",
}

# ---------------------------------------------------------------------------
# PODUJATIA (poradie = poradie na webe)
#   bzuco: {"detail": id}               -> celý Bzuco predaj pre 1 podujatie
#          {"list": [id]}               -> zoznam s filtrom (singleAuto otvorí detail)
#          {"headless": id, tiers: ...} -> vlastné karty vstupeniek + tlačidlá Bzuco
#          None                         -> predaj ešte nie je nastavený
# ---------------------------------------------------------------------------
EVENTS = [
    {
        "key": "bsf",
        "slug": "big-summer-fest-2027",
        "name": "BIG SUMMER FEST 2027",
        "short": "Big Summer Fest",
        "logo": "img/logo-bsf.webp",
        "logo_w": 640, "logo_h": 623,
        "kind": "Festival · 3 dni",
        "kicker": "Najväčší festival legendárnych hitov",
        "tile_date": "29. – 31. 7. 2027",
        "date": "29. – 31. 7. 2027",
        "date_long": "štvrtok 29. – sobota 31. júla 2027",
        "time": "štart 29. 7. o 15:00",
        "time_main": "15:00", "card_time": "", "time_sub": "štart vo štvrtok 29. 7.",
        "venue": "Zelená Voda",
        "city": "Nové Mesto nad Váhom",
        "iso_start": "2027-07-29T15:00:00+02:00",
        "iso_end": "2027-07-31T23:59:00+02:00",
        "tile_extra": "Vengaboys · Loona · Las Ketchup · Rednex · Lunetic",
        "summary": "Tretí ročník festivalu hitov 90. rokov a milénia. Viac ako 35 umelcov naživo, 3 dni plné hudby a areál pri vode.",
        "stub_label": "Vstupenky od",
        "stub_value": "99,90 €",
        "stub_note": "Limitovaný predpredaj",
        "chips_title": "Zatiaľ odhalení interpreti",
        "chips": ["Vengaboys", "Loona", "Las Ketchup", "Rednex", "Lunetic"],
        "chips_more": "ďalší čoskoro",
        "poster": "img/bsf-poster.webp",
        "countdown": {"to": "2027-07-29T15:00:00+02:00", "label": "Do festivalu zostáva"},
        "tile_img": "img/bsf-tile.webp", "tile_pos": "48% 40%",
        "hero_img": "img/bsf-hero.webp", "hero_pos": "50% 45%",
        "gallery": ["img/bsf-g1.webp", "img/bsf-g2.webp", "img/bsf-g3.webp", "img/bsf-g4.webp",
                    "img/bsf-g5.webp", "img/bsf-g6.webp", "img/bsf-g7.webp", "img/bsf-g8.webp"],
        "gallery_ratio": "4 / 3",
        "og": "img/og-bsf.jpg",
        "live_url": "https://www.superticket.sk/big-summer-fest-2027",
        "about": [
            "Zažite nezabudnuteľný návrat do minulosti na BIG SUMMER FEST 2027! Najväčší retro/nostalgia festival v strednej Európe!",
            "Okrem najväčších hviezd 90. rokov sa môžete tešiť aj na ikonických interpretov z éry rokov 2000 – 2010. Áno, prichádza miléniová horúčka! Pripravte sa na tanečné beaty, ktoré definovali začiatok nového tisícročia.",
            "Zážitok je pre nás prvoradý! Preto sa môžete spoľahnúť, že ozvučenie, produkcia, stage a vystúpenia zostávajú na najvyššej úrovni, aby ste si každú sekundu užili naplno!",
        ],
        "highlights": [
            "Viac ako 35 umelcov naživo",
            "3 dni plné hudby, od 29. do 31. júla",
            "Areál Zelená Voda s vodnou plochou a dovolenkovou atmosférou",
            "Mená interpretov odhaľujeme postupne",
        ],
        "info": [
            "ZŤP – zdarma iba vozíčkari",
            "Deti do 10 rokov (do 140 cm) zdarma",
        ],
        "links": [
            ("Oficiálny web festivalu bigsummerfest.sk", "https://bigsummerfest.sk/"),
            ("Udalosť na Facebooku", "https://fb.me/e/dk8NOdXFZ"),
        ],
        # --- obsah prevzatý zo superticket.sk/big-summer-fest-2027 ---
        "presale": {"title": "Limitovaný predpredaj", "text": "prvých 3 000 vstupeniek", "price": "99,90 € / 3 dni"},
        "lineup_title": "Zatiaľ odhalené mená",
        "lineup_note": "VENGABOYS / LAS KETCHUP / LOONA / REDNEX / LUNETIC",
        "lineup_cards": [
            {"name": "Vengaboys", "badge": "Premiéra na BSF", "tone": "#FF3F5E", "songs": ["We're Going to Ibiza!", "Boom, Boom, Boom, Boom!!", "We Like to Party!"]},
            {"name": "Loona", "badge": "Návrat", "tone": "#2F8FF0", "songs": ["Bailando", "Hijo de la Luna", "Vamos a la Playa"]},
            {"name": "Las Ketchup", "badge": "Prvýkrát na Slovensku", "tone": "#12C29A", "songs": ["Aserejé", "Kusha Las Payas", "Un Blodymary"]},
            {"name": "Rednex", "badge": "Návrat", "tone": "#F0443A", "songs": ["Cotton Eye Joe", "Old Pop in an Oak", "Wish You Were Here"]},
            {"name": "Lunetic", "badge": "Návrat", "tone": "#F5B800", "songs": ["Máma", "Ať je hudba tvůj lék", "Nohama na zemi"]},
            {"name": "???", "badge": "Čoskoro", "tone": "#151821", "songs": [], "soon": "Odhaľujeme čoskoro ďalšie meno"},
        ],
        "features_title": "Tretí ročník BIG SUMMER FEST",
        "features": [
            ("Viac ako 35 umelcov naživo", "Čaká vás nabitý line-up plný svetových mien a legiend, ktoré poznáte z rádií a klubov."),
            ("3 dni plné hudby", "Pripravte si energiu – od 29. do 31. júla sa nezastavíme ani na minútu."),
            ("Nádherný areál Zelená Voda", "Unikátne prostredie s vodnou plochou, ktorá dodáva akcii tú pravú dovolenkovú atmosféru."),
            ("Svetové hviezdy na dosah", "Mená interpretov budeme postupne odhaľovať."),
        ],
        "statement": "Tretí ročník: Najväčší festival LEGENDÁRNYCH HITOV väčší a lepší ako kedykoľvek predtým!",
        "web_cta": {"title": "Viac info na webe festivalu", "url": "https://bigsummerfest.sk/", "label": "bigsummerfest.sk"},
        "fb_event": "https://fb.me/e/dk8NOdXFZ",
        "vip_title": "VIP obsahuje",
        "vip": ["Vlastnú VIP sekciu + samostatnú tribúnu s top výhľadom na stage", "Samostatný vstup a toalety", "Parkovanie VIP grátis", "Vlastný bar"],
        "premium_title": "PREMIUM obsahuje",
        "premium": ["Sekciu na státie priamo pred pódiom"],
        "bzuco": {
            "headless": 247,
            "tiers": [
                {"name": "3-dňová vstupenka", "big": "3", "sub": "3-dňový vstup", "price": "99,90 €", "block": 1148,
                 "perks": ["Vstup na všetky 3 dni festivalu"], "note": "Limitovaný predpredaj"},
                {"name": "PREMIUM 3 dni", "big": "PREMIUM", "sub": "Státie pred pódiom", "price": "179,90 €", "block": 1150, "featured": True,
                 "perks": ["3-dňový vstup", "Sekcia na státie priamo pred pódiom"],
                 "note": "Limitovaný predpredaj"},
                {"name": "VIP 3 dni", "big": "VIP", "sub": "VIP 3-dňový vstup", "price": "399,90 €", "block": 1149,
                 "perks": ["Vlastná VIP sekcia + samostatná tribúna s top výhľadom na stage",
                           "Samostatný vstup a toalety", "Parkovanie VIP grátis", "Vlastný bar"],
                 "note": "Limitovaný predpredaj"},
            ],
        },
    },
    {
        "key": "gims",
        "slug": "gims",
        "name": "GIMS",
        "short": "GIMS",
        "logo": "img/logo-gims.webp",
        "logo_w": 900, "logo_h": 190,
        "kind": "Koncert",
        "kicker": "Francúzska hudobná senzácia",
        "tile_date": "15. 10. 2026",
        "date": "15. 10. 2026",
        "date_long": "štvrtok 15. októbra 2026",
        "time": "20:00",
        "time_main": "20:00", "card_time": "20:00", "time_sub": "odporúčame prísť o 30 min skôr",
        "venue": "Gopass Aréna",
        "city": "Bratislava",
        "iso_start": "2026-10-15T20:00:00+02:00",
        "iso_end": None,
        "tile_extra": "Spider · Bella · Hola Señorita · Parisienne",
        "summary": "Svetoznámy spevák a raper prichádza na Slovensko so strhujúcou energiou a mixom popu, hip-hopu a R&B.",
        "stub_label": "Aktuálne",
        "stub_value": "2. cenová vlna",
        "stub_note": "",
        "chips_title": "Svetové hity naživo",
        "chips": ["Spider", "Bella", "Hola Señorita", "Parisienne", "Ninao"],
        "chips_more": "",
        "poster": "img/gims-poster.webp",
        "countdown": {"to": "2026-10-15T20:00:00+02:00", "label": "Do koncertu zostáva"},
        # cenová vlna – keď poznáte koniec, doplňte napr. {"label": "2. cenová vlna", "end_label": "Koniec 2. cenovej vlny", "ends": "2026-09-30T23:59:59+02:00", "ends_text": "30. 9. 2026 o 23:59"}
        "wave": None,
        "tile_img": "img/gims-tile.webp", "tile_pos": "50% 30%",
        "hero_img": "img/gims-hero.webp", "hero_pos": "62% 40%",
        "gallery": ["img/gims-g1.webp", "img/gims-g2.webp", "img/gims-g3.webp", "img/gims-g4.webp"],
        "gallery_ratio": "3 / 4",
        "og": "img/og-gims.jpg",
        "live_url": "https://www.superticket.sk/gims",
        "about": [
            "Pripravte sa na nezabudnuteľnú show! Svetoznámy spevák a raper GIMS (predtým známy aj ako Maître Gims) prichádza na Slovensko, aby priniesol svoju strhujúcu energiu a jedinečný mix popu, hip-hopu a R&B. Zažite naživo umelca, ktorého hity s miliardami zhliadnutí dobyli svetové hitparády.",
            "Príďte si zaspievať megahity ako Spider, Bella, Hola Señorita, Parisienne či Ninao a užite si koncert plný skvelej hudby a vizuálnych zážitkov s jedným z najvýraznejších hlasov súčasnosti.",
            "Čaká vás top produkcia: ozvučenie a osvetlenie zabezpečuje MINISTRY rental service.",
        ],
        "highlights": [],
        "vip_title": "VIP vstupenka obsahuje",
        "vip": ["Welcome drink", "Najlepší výhľad z vlastnej časti tribúny", "Vlastnú VIP sekciu a toalety", "VIP vstup"],
        "info": [
            "Odporúčame prísť aspoň 30 minút pred koncertom",
            "ZŤP – vozíčkari majú vstup zdarma",
        ],
        "links": [("Oficiálny web koncertu", "https://koncertgims.eu/")],
        "bzuco": {"detail": 244},
    },
    {
        "key": "t90",
        "slug": "tvoja90kosice",
        "name": "Tvoja 90's & Millenium Show",
        "short": "Tvoja 90's Show",
        "logo": "img/logo-tvoja90s.webp",
        "logo_w": 680, "logo_h": 610,
        "kind": "Show · 90's + Millenium",
        "kicker": "Najväčšia 90's a Millenium show na Slovensku",
        "tile_date": "18. 12. 2026",
        "date": "18. 12. 2026",
        "date_long": "piatok 18. decembra 2026",
        "time": "18:00 · DJ warm-up od 17:00",
        "time_main": "18:00", "card_time": "18:00", "time_sub": "DJ warm-up od 17:00",
        "venue": "Steel Aréna",
        "city": "Košice",
        "iso_start": "2026-12-18T18:00:00+01:00",
        "iso_end": None,
        "tile_extra": "12 interpretov · 360° pódium · 5 hodín hitov",
        "summary": "2. ročník najväčšej show hviezd 90. rokov a milénia. 12 interpretov naživo, 5 hodín hitov a 360° pódium uprostred arény.",
        "stub_label": "Aktuálne",
        "stub_value": "2. cenová vlna",
        "stub_note": "",
        "chips_title": "Line-up",
        "chips": ["Vengaboys", "Loona", "Kate Ryan", "Lou Bega", "Fun Factory", "Rednex",
                  "Masterboy & Beatrix Delgado", "LayZee aka Mr. President", "Lunetic", "Karma", "Emily", "Lobo"],
        "chips_more": "",
        "poster": "img/t90-poster.webp",
        "countdown": {"to": "2026-12-18T18:00:00+01:00", "label": "Do show zostáva"},
        "wave": {"label": "2. cenová vlna", "end_label": "Koniec 2. cenovej vlny", "ends": "2026-10-15T23:59:59+02:00", "ends_text": "15. 10. 2026 o 23:59"},
        "tile_img": "img/t90-tile.webp", "tile_pos": "47% 62%",
        "hero_img": "img/t90-hero.webp", "hero_pos": "50% 40%",
        "gallery": ["img/t90-g1.webp", "img/t90-g2.webp", "img/t90-g3.webp", "img/t90-g4.webp"],
        "gallery_ratio": "4 / 3",
        "og": "img/og-t90.jpg",
        "live_url": "https://www.superticket.sk/tvoja90kosice",
        "about": [
            "Po obrovskom úspechu prvého ročníka prichádza pokračovanie! Pripravte sa na ešte väčšiu nálož nostalgie a tanečnej energie. Tvoja 90's SHOW hlási návrat a tentokrát sa celá show sústredí exkluzívne na východ Slovenska.",
            "Čaká vás 5 hodín tých najväčších hitov, špeciálne svetelné a vizuálne efekty, laserová show, obrovské LED obrazovky a pyrotechnika.",
            "DJ warm-up začína už o 17:00. Bary, občerstvenie a tá najlepšia nálada na vás čakajú hneď od otvorenia brán. O atmosféru sa postarajú skvelí moderátori večera.",
        ],
        "highlights": [
            "360° pódium – perfektný výhľad z každého miesta",
            "12 interpretov 90. rokov a milénia naživo",
            "5 hodín hitov, laserová show a pyrotechnika",
        ],
        "vip_title": "VIP vstupenka obsahuje",
        "vip": ["Sektor A12", "Exkluzívnu VIP zónu v rámci sektora A12",
                "VIP catering – teplý a studený bufet vo vyhradenej VIP zóne", "Víno, prosecco, pivo a nealko"],
        "info": [
            "Odporúčame prísť aspoň 30 minút pred koncertom",
            "ZŤP – vozíčkari majú vstup zdarma",
            "Zmena programu a cien vyhradená",
        ],
        "links": [("Oficiálny web show", "https://tvoja90s.sk/")],
        "bzuco": {"list": [245]},
    },
    {
        "key": "lun",
        "slug": "30-rokov-lunetic",
        "name": "30 rokov LUNETIC",
        "short": "30 rokov Lunetic",
        "logo": "img/logo-lunetic30.webp",
        "logo_w": 900, "logo_h": 305,
        "kind": "Výročný koncert",
        "kicker": "Sólo koncert kapely k 30. výročiu",
        "tile_date": "8. 10. 2027",
        "date": "8. 10. 2027",
        "date_long": "piatok 8. októbra 2027",
        "time": "",
        "time_main": "Upresníme", "card_time": "", "time_sub": "",
        "venue": "Gopass Aréna",
        "city": "Bratislava",
        "iso_start": "2027-10-08",
        "iso_end": None,
        "tile_extra": "Sólo koncert · 30. výročie",
        "summary": "Lunetic oslavuje 30 rokov na scéne veľkým sólo koncertom v Gopass Aréne. Ich hity žijú ďalej.",
        "stub_label": "Výročie",
        "stub_value": "30 rokov na scéne",
        "stub_note": "",
        "chips_title": "",
        "chips": [],
        "chips_more": "",
        "poster": "img/lun-poster.webp",
        "countdown": {"to": "2027-10-08T00:00:00+02:00", "label": "Do koncertu zostáva"},
        "tile_img": "img/lun-tile.webp", "tile_pos": "50% 55%",
        "hero_img": "img/lun-hero.webp", "hero_pos": "50% 50%",
        "gallery": ["img/lun-g1.webp", "img/lun-g2.webp", "img/lun-g3.webp", "img/lun-g4.webp"],
        "gallery_ratio": "4 / 3",
        "og": "img/og-lun.jpg",
        "live_url": "https://www.superticket.sk/",
        "about": [
            "Lunetic oslavuje 30 rokov na scéne a pozýva vás na veľký sólo koncert do Gopass Arény v Bratislave.",
            "Podrobnosti k programu zverejníme čoskoro. Sledujte novinky na superticket.sk a na našich sociálnych sieťach.",
        ],
        "highlights": [],
        "info": ["Odporúčame prísť aspoň 30 minút pred koncertom"],
        "links": [],
        "bzuco": None,   # TODO: doplniť ID podujatia z Bzuco, napr. {"detail": 250}
    },
]

# ---------------------------------------------------------------------------
# NOVINKY A ZMENY (najnovšie hore). tag: "novinka" | "zmena" | "info"
# date je nepovinný – ak ho vyplníte, zobrazí sa (napr. "28. 9. 2026")
# ---------------------------------------------------------------------------
NEWS = [
    {"tag": "novinka", "date": "28. 9. 2026", "event": "lun",
     "title": "30 rokov LUNETIC v Gopass Aréne",
     "text": "Výročný sólo koncert kapely Lunetic sa uskutoční 8. 10. 2027 v Bratislave."},
    {"tag": "novinka", "date": "28. 9. 2026", "event": "bsf",
     "title": "BIG SUMMER FEST 2027: prvé mená",
     "text": "Zatiaľ odhalení: Vengaboys, Loona, Las Ketchup, Rednex a Lunetic. Ďalšie mená postupne."},
    {"tag": "novinka", "date": "28. 9. 2026", "event": "t90",
     "title": "Tvoja 90's Show Košice: kompletný line-up",
     "text": "12 interpretov naživo vrátane Vengaboys, Loona, Kate Ryan a Lou Bega."},
    {"tag": "info", "date": "28. 9. 2026", "event": "gims",
     "title": "GIMS: prebieha 2. cenová vlna",
     "text": "Koncert 15. 10. 2026 o 20:00 v Gopass Aréne. Odporúčame prísť aspoň 30 minút vopred."},
]

# ---------------------------------------------------------------------------
# MINULÉ AKCIE – bannery 1100 × 413 px v img/minule/ (+ zmenšenina -sm)
# ---------------------------------------------------------------------------
PAST = [
    ("2025", [
        {"slug": "bsf-2025", "title": "BIG SUMMER FEST 90's", "sub": "1. – 2. 8. 2025 · Zelená Voda, Nové Mesto nad Váhom", "kind": "Festival", "video": "https://www.youtube.com/watch?v=AnWtV9F3lDM", "tone": "#FF9F1C"},
        {"slug": "karol-duchon-75", "title": "Karol Duchoň 75 – Megakoncert", "sub": "Turné 6 miest", "kind": "Turné", "video": "https://www.youtube.com/watch?v=QZ9AC3VLPSo", "tone": "#B03FC8"},
        {"slug": "desmod-open-air", "title": "Desmod – Open Air", "sub": "Terchová", "kind": "Koncert", "video": "", "tone": "#2B55C9"},
        {"slug": "nikolas-put", "title": "Nikolas Put – Spomienkový koncert piesní Karla Gotta", "sub": "Koncertné turné viac ako 15 miest", "kind": "Turné", "video": "", "tone": "#C9962E"},
        {"slug": "mioli", "title": "MiOli – nová hudobná show pre deti", "sub": "Tour 2025 · až 25 miest", "kind": "Pre deti", "video": "", "tone": "#C0283B"},
    ]),
    ("2024", [
        {"slug": "kabat-35-let", "title": "Kabát – 35 let", "sub": "Bratislava · Zvolen · Košice · Poprad", "kind": "Turné", "video": "https://www.youtube.com/watch?v=qzzdj9_gXo0", "tone": "#5B5F68"},
        {"slug": "tvoja-90s-show", "title": "Tvoja 90's Show", "sub": "Bratislava a Košice", "kind": "Show", "video": "https://www.youtube.com/watch?v=Kgjwl98VU9Y", "tone": "#7B2BD1"},
        {"slug": "killer-queen", "title": "Killer Queen – Tribute to Queen", "sub": "Legendárna Queen show z Londýna", "kind": "Koncert", "video": "https://www.youtube.com/watch?v=ijyFLQE9iVg", "tone": "#1F4FA8"},
        {"slug": "abba-mania", "title": "ABBA Mania by ABBA Stars", "sub": "Turné jeseň 2024", "kind": "Turné", "video": "https://www.youtube.com/watch?v=SoqN5Cm8lEA", "tone": "#A57F2E"},
        {"slug": "smolkovia", "title": "Šmolkovia – hudobný muzikál pre deti", "sub": "Tour 2024", "kind": "Pre deti", "video": "", "tone": "#2E8FD6"},
        {"slug": "masa-a-medved", "title": "Máša a Medveď – muzikál pre deti", "sub": "35 slovenských miest", "kind": "Pre deti", "video": "", "tone": "#D6336C"},
    ]),
]

# ---------------------------------------------------------------------------
# ODZNAK NAD PÄTIČKOU (čísla od vás)
# ---------------------------------------------------------------------------
STATS = [
    {"value": 5, "suffix": "+", "label": "rokov na trhu", "icon": "clock"},
    {"value": 150000, "suffix": "+", "label": "spokojných zákazníkov", "icon": "users"},
    {"value": 3, "suffix": "", "label": "krajiny", "icon": "globe"},
    {"value": 250, "suffix": "+", "label": "podujatí", "icon": "ticket"},
]

# Weby podujatí – mini sekcia na stránke Kontakt
WEBS = [
    {"name": "BIG SUMMER FEST", "url": "https://bigsummerfest.sk/", "domain": "bigsummerfest.sk", "logo": "img/logo-bsf.webp", "key": "bsf"},
    {"name": "Tvoja 90's Show", "url": "https://tvoja90s.sk/", "domain": "tvoja90s.sk", "logo": "img/logo-tvoja90s.webp", "key": "t90"},
    {"name": "LUNETIC", "url": "https://lunetic.sk/", "domain": "lunetic.sk", "logo": "img/logo-lunetic30.webp", "key": "lun"},
]

# ---------------------------------------------------------------------------
# ČASTÉ OTÁZKY – text prevzatý zo superticket.sk/caste-otazky, rozdelený do skupín
# ---------------------------------------------------------------------------
S = CONTACT["support"]
_mail = lambda m: f'<a href="mailto:{m}">{m}</a>'
FAQ = [
    ("nakup", "Nákup vstupeniek", [
        ("Musím sa registrovať, ak si chcem kúpiť vstupenky?",
         "<p>Vstupenky si môžete zakúpiť aj bez registrácie a bez vytvorenia účtu.</p>"),
        ("Aký je limit vstupeniek na jednu objednávku?",
         "<p>Na jednu objednávku je zvyčajne možné zakúpiť maximálne 15 vstupeniek. Maximálny počet môže byť ovplyvnený špecifickými podmienkami jednotlivých podujatí.</p>"),
        ("Považujú sa vstupenky v košíku za záväznú objednávku?",
         "<p>Objednávka v košíku nie je záväzná. Ak do 20 minút nezaplatíte a nedokončíte objednávku, vstupenky sa automaticky uvoľnia a objednávka sa zruší.</p>"),
        ("Je možné si vstupenky rezervovať?", "<p>Rezervácia vstupeniek nie je možná.</p>"),
        ("Môžem zakúpiť vstupenky na niekoľko podujatí naraz?",
         "<p>Áno, môžete si zakúpiť vstupenky na viacero našich podujatí súčasne. Stačí si vybrať podujatia, ktoré vás zaujímajú, a pokračovať v objednávke pre každé z nich.</p>"),
        ("Poskytujete zľavy na vstupenky pre deti, študentov a ZŤP?",
         "<p>Pokiaľ nie je v popise podujatia uvedené inak, na dané podujatie sa nevzťahujú žiadne zľavy. Dôležité je tiež poznamenať, že každý návštevník podujatia musí mať vlastnú vstupenku.</p>"),
    ]),
    ("platba", "Platba", [
        ("Aké sú spôsoby platby za vstupenky?",
         "<ul><li><strong>Platobná karta</strong> – akceptujeme karty Visa a Mastercard. Platba je realizovaná prostredníctvom zabezpečenej platobnej brány.</li>"
         "<li><strong>Rýchly bankový prevod</strong> – podporujeme okamžité bankové prevody cez TatraPay, VÚB, UniCredit, SporoPay a Poštovú banku. Po výbere tejto možnosti budete presmerovaní na internet banking vašej banky, kde jednoducho potvrdíte platbu. Všetky údaje o platbe, vrátane čísla účtu, variabilného symbolu a sumy objednávky, budú automaticky predvyplnené.</li>"
         "<li><strong>Google Pay</strong> – pre rýchlu a bezpečnú platbu môžete využiť digitálnu peňaženku Google Pay.</li></ul>"),
        ("Je možná platba prevodom na účet?",
         "<p>Platba prevodom nie je možná. Objednávku je potrebné uhradiť online priamo v procese objednávky.</p>"),
        ("Ako zistím, že moja platba bola úspešná?",
         f"<p>Po úspešnej realizácii platby vám na e-mail uvedený v objednávke zašleme potvrdenie o úspešnej platbe spolu so zakúpenými vstupenkami. Ak potvrdenie neobdržíte, skontrolujte aj nevyžiadanú poštu (spam).</p><p>V prípade, že vstupenky nenájdete, kontaktujte nás na {_mail(S)} (Po – Pi 09:00 – 16:00). V správe, prosím, uveďte meno a e-mail objednávateľa.</p>"),
        ("Čo robiť, ak mám problém pri platbe kartou?",
         "<p>Uistite sa, že máte správne číslo karty, dátum platnosti a 3-miestny bezpečnostný kód CVC. Okrem toho skontrolujte, či máte vo svojom internetovom bankovníctve povolené platby kartou online a či máte nastavený limit pre tieto platby. Ak máte všetko správne nastavené, platba by mala prebehnúť bez problémov.</p>"),
        ("Čo mám robiť, ak sa platbu kartou opakovane nepodarilo dokončiť?",
         "<p>Ak platba opakovane neprebehne a všetky zadané údaje karty sú správne, odporúčame vám obrátiť sa na svoju banku a overiť si, či vaša karta podporuje nákupy online a či máte nastavený limit pre tento typ platby. Objednávku musíte uhradiť len spôsobmi uvedenými priamo v procese objednávky.</p>"),
    ]),
    ("dorucenie", "Doručenie a vstup na podujatie", [
        ("Ako sa dostanem k zakúpeným vstupenkám?",
         "<p>Vstupenky vám budú zaslané automaticky na vami zadanú e-mailovú adresu ako príloha e-mailu od odosielateľa <strong>vstupenky@superticket.sk</strong>. Každá vstupenka slúži na jednorazový vstup.</p>"),
        ("Musím si zakúpené vstupenky vytlačiť?",
         "<p>Vstupenky nie je potrebné tlačiť, pretože naše digitálne vstupenky obsahujú QR kód, ktorý pri vstupe na podujatie jednoducho ukážete na displeji mobilného telefónu. Odporúčame preto, aby ste si stiahnuté vstupenky pripravili vopred.</p>"),
        ("Na čo slúži QR kód?",
         "<p>QR kód je špeciálny kód, ktorý v sebe obsahuje informáciu o podujatí a vstupenke. Každá vstupenka obsahuje unikátny QR kód. Po vstupe a overení špeciálnou čítačkou sa kód na vstupenke deaktivuje a nie je možné ho použiť viackrát.</p><p>Je dôležité, aby ste svoju vstupenku (QR kód) nenechali skopírovať inou osobou, nezverejňovali fotografie vstupeniek na sociálnych sieťach a nevytvárali zbytočné kópie – predídete tým zneužitiu vašej vstupenky. Pre niektoré podujatia môžu byť alternatívou ku QR kódu aj čiarové kódy.</p>"),
        ("Čo mám robiť, ak som zaplatil/a za svoju objednávku, ale nedostal/a som vstupenky na e-mail?",
         f"<p>Aby ste sa vyhli problémom s doručením, odporúčame použiť e-mailové služby ako Gmail, iCloud alebo ProtonMail, ktoré spoľahlivo prijímajú naše správy. Naopak, Yahoo, Outlook (Hotmail, Live) a AOL častejšie blokujú alebo filtrujú e-maily do spamu, čo môže spôsobiť, že vaša vstupenka nepríde. Ak ste nedostali potvrdzujúci e-mail, skontrolujte aj priečinok s nevyžiadanou poštou (spam).</p><p>Ak potvrdenie objednávky stále nenájdete, kontaktujte našu podporu na adrese {_mail(S)} (Po – Pi 09:00 – 16:00). V správe, prosím, uveďte meno a e-mail objednávateľa, prípadne číslo objednávky.</p>"),
        ("Čo mám robiť, ak som si kúpil/a lístok tesne pred podujatím, ale neprišiel mi na e-mail?",
         "<p>V prípade, že ste si vstupenky objednali tesne pred podujatím a z akéhokoľvek dôvodu ste ich nedostali, pokojne príďte na miesto konania s potvrdením o platbe – na mieste vám radi pomôžeme.</p>"),
        ("Aké predmety si môžem vziať so sebou na koncert/festival?",
         "<p>Vždy si so sebou vezmite len to najnutnejšie, aby ste sa vyhli radom a zbytočným problémom pri vstupe. Na koncerty a festivaly si nesmiete brať občerstvenie (vrátane vody), dáždniky, stoličky, zvieratá, nože alebo iné zbrane či omamné látky.</p>"),
    ]),
    ("storno", "Storno, zmeny a vrátenie peňazí", [
        ("Aké sú pravidlá stornovania vstupeniek?",
         "<p>Podľa Všeobecných obchodných podmienok je storno zakúpených vstupeniek možné len v prípade zmeny dátumu/času alebo miesta konania podujatia alebo v prípade úplného zrušenia podujatia organizátorom. Ak dôjde k niektorej z týchto zmien, automaticky vás informujeme a riešime ďalšie kroky.</p>"),
        ("Čo sa stane, ak sa podujatie zruší alebo presunie na iný termín?",
         "<p>O zrušení alebo preložení podujatia vás budeme včas informovať na vami zadanú e-mailovú adresu. V prípade zrušenia podujatia má držiteľ vstupenky nárok na vrátenie peňazí spôsobom určeným organizátorom.</p>"),
        ("Aké sú podmienky pre vrátenie peňazí pri zrušení podujatia?",
         "<p>V prípade zrušenia podujatia vám vrátime peniaze výhradne na účet, z ktorého bola objednávka zaplatená. Nie je potrebné zasielať žiadne ďalšie údaje, ako je IBAN alebo číslo účtu – všetky informácie budú spracované automaticky na základe pôvodnej platby.</p>"),
        ("Je možná výmena lístkov?",
         f"<p>Výmena lístkov je možná, ale žiadame vás, aby ste nás o tejto zmene informovali najmenej týždeň pred konaním podujatia. Pri výmene je potrebné uviesť:</p><ul><li>meno a e-mail, na ktoré bola objednávka vytvorená,</li><li>ID objednávky,</li><li>mesto, do ktorého chcete lístky vymeniť,</li><li>požiadavky na konkrétne miesta na sedenie, ak je to relevantné.</li></ul><p>Výmena je možná len v rámci rovnakej cenovej kategórie lístkov, ako boli pôvodne zakúpené. V prípade, že sú voľné len lístky v nižšej cenovej kategórii, výmena je stále možná, avšak rozdiel v cene nevraciame.</p><p>Výmena lístkov je možná iba na rovnaké podujatie (do iného mesta), ako máte zakúpené vstupenky – lístky z jedného koncertu nie je možné vymeniť na úplne iné podujatie.</p><p>Všetky žiadosti o výmenu lístkov riešime výhradne e-mailom na {_mail(S)} (Po – Pi 09:00 – 16:00).</p>"),
    ]),
    ("spoluprace", "Spolupráce", [
        ("Máme záujem o spoluprácu. Kam sa môžeme obrátiť?",
         f"<p>V prípade, že máte záujem o spoluprácu, kontaktujte nás na {_mail(CONTACT['marketing'])} (Po – Pi 09:00 – 16:00).</p>"),
    ]),
]


# ---------------------------------------------------------------------------
# REFERENCIE – logá akcií pre pohyblivú vitrínu na úvode (img/ref/*.webp)
# dark=True -> logo na tmavej dlaždici (zlaté/žlté logá)
# ---------------------------------------------------------------------------
REFS = [
    {"slug": "bsf-2026", "name": "BIG SUMMER FEST 2026"},
    {"slug": "abba-mania", "name": "ABBA Mania by ABBA Stars", "dark": True},
    {"slug": "tvoja-90s", "name": "Tvoja 90's Show"},
    {"slug": "harlem", "name": "Harlem Globetrotters 2024 World Tour"},
    {"slug": "kiss-party", "name": "Kiss Party 2025"},
    {"slug": "killer-queen", "name": "Killer Queen – Tribute to Queen", "dark": True},
    {"slug": "masa-a-medved", "name": "Máša a Medveď"},
    {"slug": "bsf-2025", "name": "BIG SUMMER FEST 90's 2025"},
    {"slug": "mega-kiss-party", "name": "Mega Kiss Party"},
    {"slug": "dj-smajlik", "name": "DJ Smajlík", "dark": True},
    {"slug": "smolkovia", "name": "Šmolkovia"},
]

# Sociálne siete – stránka Kontakt
SOCIAL = [
    {"name": "Facebook", "handle": "superticket.sk", "url": "https://www.facebook.com/superticket.sk", "icon": "fb", "text": "Novinky, odhalené mená a zmeny podujatí"},
    {"name": "Instagram", "handle": "@superticket.sk", "url": "https://www.instagram.com/superticket.sk/", "icon": "ig", "text": "Fotky a videá z našich akcií"},
]
