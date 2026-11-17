#!/usr/bin/env python3
import html
import json
import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
APP = json.loads((ROOT / "content/app.json").read_text(encoding="utf-8"))
SHOTS = json.loads((ROOT / "content/screenshots.json").read_text(encoding="utf-8"))
FEATURES = json.loads((ROOT / "content/features.json").read_text(encoding="utf-8"))
BASE = APP["website_url"].rstrip("/")
PLAY = APP["google_play_url"]

DATA = [
    ("slice-with-precision", "How to slice fruit with better timing and precision", "كيف تقطّع الفواكه بتوقيت ودقة أفضل",
     "Learn the simple habits behind cleaner swipes, accurate cuts and more consistent arcade runs.",
     "تعرّف على عادات بسيطة تساعدك على السحب بدقة وتحقيق ضربات أنظف وجولات أكثر اتساقاً.",
     [
       ("Watch the fruit, not just the score", "راقب الفواكه ولا تنشغل بالنتيجة", "Keep your attention on the objects entering the play area. Notice their direction and timing before making a swipe.", "ركّز على الأجسام التي تدخل مساحة اللعب. لاحظ اتجاهها وتوقيت ظهورها قبل تنفيذ حركة السحب."),
       ("Use deliberate swipes", "استخدم حركات سحب محسوبة", "Make clear, controlled swipes across fruit. Rushed or poorly aimed movements can miss targets or create avoidable mistakes.", "نفّذ حركات سحب واضحة ومتحكماً بها عبر الفواكه. قد تؤدي الحركات المتسرعة أو غير الدقيقة إلى تفويت الأهداف أو ارتكاب أخطاء."),
       ("React to changing patterns", "تفاعل مع الأنماط المتغيرة", "As levels progress, object speed and spawn patterns can become more demanding. Adjust your timing instead of repeating the same movement.", "مع التقدم في المستويات، قد تصبح سرعة الأجسام وأنماط ظهورها أكثر تطلباً. عدّل توقيتك بدلاً من تكرار الحركة نفسها."),
       ("Practice consistency", "تدرّب على الثبات", "A steady run comes from combining accuracy with quick reactions. Focus on making each swipe count rather than moving constantly.", "تأتي الجولة الجيدة من الجمع بين الدقة وسرعة الاستجابة. ركّز على فاعلية كل حركة بدلاً من السحب المستمر.")
     ]),
    ("build-combo-chains", "How to build longer fruit-slicing combo chains", "كيف تبني سلاسل كومبو أطول عند تقطيع الفواكه",
     "Understand how quick successive slices support combo streaks and help you push for a higher score.",
     "افهم كيف تساعد الضربات المتتابعة السريعة على بناء سلاسل كومبو ومواصلة السعي إلى نتيجة أعلى.",
     [
       ("Look for groups of fruit", "ابحث عن مجموعات الفواكه", "Watch for fruit appearing close together and plan a clean swipe that reaches multiple safe targets.", "راقب ظهور الفواكه متقاربة، وخطط لحركة سحب دقيقة تصل إلى عدة أهداف آمنة."),
       ("Keep your rhythm", "حافظ على إيقاعك", "Combo chains reward quick successive slices. Balance speed with control so that a longer streak does not become a careless swipe.", "تكافئ سلاسل الكومبو الضربات السريعة المتتابعة. وازن بين السرعة والتحكم حتى لا تتحول السلسلة الطويلة إلى حركة غير محسوبة."),
       ("Stay aware of hazards", "انتبه إلى المخاطر", "Never chase a combo blindly. Check the play area for bombs before extending a streak.", "لا تطارد الكومبو دون انتباه. افحص مساحة اللعب بحثاً عن القنابل قبل مواصلة السلسلة."),
       ("Learn from each run", "استفد من كل جولة", "Use your score and best-score progress as feedback. Notice which movements worked and where timing can improve.", "استخدم نتيجتك وتقدم أفضل نتيجة كمؤشر للتعلم. لاحظ الحركات الناجحة والمواضع التي يمكن تحسين توقيتها.")
     ]),
    ("avoid-bombs", "How to avoid bombs in a fruit-slicing arcade game", "كيف تتجنب القنابل في لعبة أركيد لتقطيع الفواكه",
     "Stay alert when fruit and hazards appear together. Careful target selection matters as much as speed.",
     "حافظ على انتباهك عند ظهور الفواكه والمخاطر معاً. اختيار الأهداف بعناية لا يقل أهمية عن السرعة.",
     [
       ("Identify the target first", "حدّد الهدف أولاً", "Take a brief moment to distinguish fruit from dangerous objects before swiping.", "خصص لحظة قصيرة للتمييز بين الفواكه والأجسام الخطيرة قبل السحب."),
       ("Do not swipe through uncertainty", "لا تسحب عندما تكون غير متأكد", "If a bomb is close to the fruit you want to slice, choose a safer movement rather than forcing the cut.", "إذا كانت قنبلة قريبة من الفاكهة التي تريد تقطيعها، فاختر حركة أكثر أماناً بدلاً من فرض الضربة."),
       ("Prioritize control over panic", "قدّم التحكم على الارتباك", "Fast reactions help, but uncontrolled movements can end a promising run. Keep your swipes deliberate.", "تساعد سرعة الاستجابة، لكن الحركات غير المنضبطة قد تنهي جولة واعدة. حافظ على سحب محسوب."),
       ("Adjust as difficulty rises", "تكيف مع ارتفاع الصعوبة", "Later levels can increase speed and challenge intensity. Stay focused and reassess the screen before each move.", "قد تزيد المستويات اللاحقة السرعة وشدة التحدي. حافظ على تركيزك وأعد تقييم الشاشة قبل كل حركة.")
     ]),
    ("levels-coins-gems", "Understanding levels, coins and gems in Fruit Fury Slice", "فهم المستويات والعملات والجواهر في Fruit Fury Slice",
     "A practical overview of the game's progression, score chasing and rewards described on Google Play.",
     "نظرة عملية على التقدم في اللعبة ومطاردة النتائج والمكافآت المذكورة في صفحة Google Play.",
     [
       ("Progress through levels", "تقدم عبر المستويات", "The game description explains that later levels introduce faster objects, changing spawn patterns and greater challenge intensity.", "يوضح وصف اللعبة أن المستويات اللاحقة تقدم أجساماً أسرع وأنماط ظهور متغيرة وتحديات أشد."),
       ("Earn in-game rewards", "اكسب المكافآت داخل اللعبة", "Coins and gems are listed among the rewards earned through gameplay progression. Their availability is part of the in-game experience.", "تُذكر العملات والجواهر ضمن المكافآت التي تُكتسب أثناء التقدم في اللعب. وهي جزء من تجربة اللعبة."),
       ("Track your score", "تابع نتيجتك", "Use the current score and best score shown in the game as simple ways to track your progress from one run to another.", "استخدم النتيجة الحالية وأفضل نتيجة المعروضتين في اللعبة لمتابعة تقدمك من جولة إلى أخرى."),
       ("Use the support store thoughtfully", "استخدم متجر الدعم بحكمة", "The published screenshot shows a Run Support Store that uses earned coins for gameplay support options. Review each option in the game before choosing.", "تُظهر إحدى لقطات الشاشة متجر دعم الجولة الذي يستخدم العملات المكتسبة لخيارات مساندة اللعب. راجع كل خيار داخل اللعبة قبل الاختيار.")
     ])
]

GUIDES = {
 "guide": ("Fruit Fury Slice gameplay guide", "دليل اللعب في Fruit Fury Slice",
           "A quick walkthrough of slicing fruit, building combos, avoiding bombs and understanding the game screens.",
           "شرح سريع لتقطيع الفواكه وبناء سلاسل الكومبو وتجنب القنابل وفهم شاشات اللعبة.",
           [
             ("Start from the game home screen", "ابدأ من الشاشة الرئيسية", "The home screen shows your current level, best score and credits, with Play, Store and Settings options.", "تعرض الشاشة الرئيسية مستواك الحالي وأفضل نتيجة ورصيدك، إلى جانب خيارات اللعب والمتجر والإعدادات."),
             ("Slice fruit during a run", "قطّع الفواكه أثناء الجولة", "Swipe across fruit as it appears. The gameplay screen displays score, coins, level, combo and a timer or target.", "اسحب عبر الفواكه عند ظهورها. تعرض شاشة اللعب النتيجة والعملات والمستوى والكومبو والمؤقت أو الهدف."),
             ("Avoid bombs and keep control", "تجنب القنابل وحافظ على التحكم", "Choose your swipes carefully. A careless movement through a bomb can end a run.", "اختر حركات السحب بعناية. قد تنهي حركة غير محسوبة تمر عبر قنبلة الجولة."),
             ("Review rewards and settings", "راجع المكافآت والإعدادات", "The screenshots show a Run Support Store and settings that include haptic feedback, privacy policy and support.", "تُظهر لقطات الشاشة متجر دعم الجولة وإعدادات تتضمن الاهتزاز اللمسي وسياسة الخصوصية والدعم.")
           ]),
 "tips": ("Fruit slicing tips for cleaner combos and higher scores", "نصائح لتقطيع أدق وسلاسل كومبو ونتائج أعلى",
          "Simple gameplay habits for better timing, safer swipes and more consistent runs.",
          "عادات لعب بسيطة لتحسين التوقيت وجعل السحب أكثر أماناً وتحقيق جولات أكثر اتساقاً.",
          [
            ("Watch before you swipe", "راقب قبل السحب", "Check the position of fruit and bombs before making a move.", "تحقق من مواقع الفواكه والقنابل قبل تنفيذ الحركة."),
            ("Aim for clean successive cuts", "استهدف ضربات متتابعة ودقيقة", "Quick, accurate slices help build combo chains and improve your score.", "تساعد الضربات السريعة والدقيقة على بناء سلاسل كومبو وتحسين نتيجتك."),
            ("Adapt to faster levels", "تكيف مع المستويات الأسرع", "Object speed and challenge intensity can rise as you progress. Adjust your reaction time.", "قد ترتفع سرعة الأجسام وشدة التحديات مع التقدم. عدّل سرعة استجابتك."),
            ("Learn from your best score", "تعلم من أفضل نتيجة", "Use your best score as a benchmark and focus on one improvement in each new run.", "استخدم أفضل نتيجة معياراً لك، وركّز على تحسين جانب واحد في كل جولة جديدة.")
          ]),
 "comparison": ("Fruit Fury Slice: quick sessions and skill-based arcade play", "Fruit Fury Slice: جولات سريعة ولعب أركيد يعتمد على المهارة",
                "What defines the game's arcade loop: quick controls, precise timing, combos, hazards and progressive challenge.",
                "ما الذي يميز دورة اللعب في الأركيد: تحكم سريع وتوقيت دقيق وكومبو ومخاطر وتحديات متدرجة.",
                [
                  ("Simple to begin", "سهلة البداية", "The core action is easy to understand: swipe to slice fruit as it appears.", "الفكرة الأساسية سهلة الفهم: اسحب لتقطيع الفواكه عند ظهورها."),
                  ("Skill matters over time", "المهارة مهمة مع الوقت", "Improving accuracy, timing and hazard awareness takes practice.", "يتطلب تحسين الدقة والتوقيت والانتباه للمخاطر بعض التدريب."),
                  ("Challenge increases", "التحدي يزداد", "Later levels increase the pace and intensity, giving players more to react to.", "ترفع المستويات اللاحقة الإيقاع وشدة التحدي، ما يتطلب استجابة أكبر."),
                  ("Play without a constant connection", "العب دون اتصال دائم", "The Google Play description states that the core arcade experience supports offline play.", "يذكر وصف Google Play أن تجربة الأركيد الأساسية تدعم اللعب دون اتصال.")
                ])
}

FEATURE_DETAILS = {
 "precision-slicing": [
   ("Read the screen", "اقرأ الشاشة", "Watch where fruit appears and choose a clear path for your swipe.", "راقب أماكن ظهور الفواكه واختر مساراً واضحاً لحركة السحب."),
   ("Time each cut", "اختر توقيت كل ضربة", "Responsive touch controls make timing and accuracy central to each slice.", "تجعل عناصر التحكم باللمس التوقيت والدقة عنصرين أساسيين في كل ضربة."),
   ("Stay consistent", "حافظ على الاتساق", "Controlled movements help you respond as object speed and patterns change.", "تساعد الحركات المنضبطة على الاستجابة عند تغير سرعة الأجسام وأنماط ظهورها.")
 ],
 "combo-chains": [
   ("Chain successive slices", "اربط الضربات المتتابعة", "Slice multiple fruits in quick succession to build combo chains.", "قطّع عدة فواكه بسرعة متتابعة لبناء سلاسل كومبو."),
   ("Balance speed and accuracy", "وازن بين السرعة والدقة", "A fast swipe only helps when it reaches the intended fruit safely.", "لا تفيد حركة السحب السريعة إلا إذا وصلت إلى الفاكهة المستهدفة بأمان."),
   ("Chase your best score", "اسعَ إلى تحسين أفضل نتيجة", "Use each run to refine your timing and push your score higher.", "استفد من كل جولة لتحسين توقيتك ورفع نتيجتك.")
 ],
 "bomb-dodging": [
   ("Recognize dangerous objects", "تعرّف على الأجسام الخطيرة", "The game includes bombs that punish careless swipes.", "تتضمن اللعبة قنابل تعاقب حركات السحب غير المحسوبة."),
   ("Choose safe paths", "اختر مسارات آمنة", "Avoid swiping through bombs even when fruit is nearby.", "تجنب السحب عبر القنابل حتى عندما تكون الفواكه قريبة."),
   ("Keep your focus", "حافظ على تركيزك", "Careful decisions help protect a promising run.", "تساعد القرارات الدقيقة على حماية الجولة الواعدة.")
 ],
 "levels-and-rewards": [
   ("Face changing challenges", "واجه تحديات متغيرة", "Object speed, spawn patterns and challenge intensity increase as levels progress.", "تزداد سرعة الأجسام وأنماط ظهورها وشدة التحديات مع التقدم في المستويات."),
   ("Collect progression rewards", "اجمع مكافآت التقدم", "The game description lists coins and gems among rewards earned during play.", "يذكر وصف اللعبة العملات والجواهر ضمن المكافآت المكتسبة أثناء اللعب."),
   ("Play on your schedule", "العب في الوقت الذي يناسبك", "The core arcade experience supports offline play, according to the Google Play description.", "تدعم تجربة الأركيد الأساسية اللعب دون اتصال، وفق وصف Google Play.")
 ]
}

def e(value):
    return html.escape(str(value), quote=True)

def route_url(lang, tail=""):
    return f"{BASE}/{lang}/" + (f"{tail}/" if tail else "")

def routes():
    tails = ["", "about", "features", "download", "faq", "blog"]
    tails += ["features/" + f["id"] for f in FEATURES]
    tails += ["blog/" + a[0] for a in DATA]
    tails += list(GUIDES)
    return [(lang, tail) for lang in ("en", "ar") for tail in tails]

def nav(lang):
    import build
    primary = {"en": [("about", "About"), ("features", "Features"), ("download", "Download"), ("faq", "FAQ")],
               "ar": [("about", "عن اللعبة"), ("features", "المزايا"), ("download", "التنزيل"), ("faq", "الأسئلة")]}
    resources = {"en": [("tips", "Tips"), ("blog", "Blog"), ("guide", "Game guide"), ("comparison", "Gameplay")],
                 "ar": [("tips", "نصائح اللعب"), ("blog", "المدونة"), ("guide", "دليل اللعبة"), ("comparison", "تجربة اللعب")]}
    primary_links = "".join(f'<a data-nav-item="{key}" href="{route_url(lang, key)}">{label}</a>' for key, label in primary[lang])
    resource_links = "".join(f'<a data-nav-item="{key}" href="{route_url(lang, key)}">{label}</a>' for key, label in resources[lang])
    tail = ""
    return (
      f'<header class="standard-header"><div class="locale-switch" aria-label="Country and region">{build.render_market_flags(tail)}{build.render_social_links()}</div>'
      f'<div class="header-main"><a class="brand" href="{BASE}/">FRUIT <b>FURY</b></a><nav aria-label="Primary navigation">'
      f'<details class="nav-menu" data-nav-group="primary"><summary>{"Explore" if lang == "en" else "استكشف"}</summary><div class="nav-dropdown">{primary_links}</div></details>'
      f'<details class="nav-menu" data-nav-group="resources"><summary>{"Gameplay" if lang == "en" else "اللعب"}</summary><div class="nav-dropdown">{resource_links}</div></details>'
      f'</nav></div></header>'
    )

def page(lang, tail, title, description, content, kind="WebPage"):
    url = route_url(lang, tail)
    organization = {"@type": "Organization", "@id": f"{BASE}/#organization", "name": APP["developer"], "url": BASE + "/", "email": APP["support_email"]}
    schema_item = {"@type": kind, "name": title, "description": description, "inLanguage": lang, "url": url, "publisher": {"@id": f"{BASE}/#organization"}}
    graph = [organization, schema_item]
    schema = {"@context": "https://schema.org", "@graph": graph}
    return f'''<!doctype html><html lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{route_url("en", tail)}"><link rel="alternate" hreflang="ar" href="{route_url("ar", tail)}"><link rel="alternate" hreflang="x-default" href="{route_url("en", tail)}"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{e(SHOTS[0]["src"])}"><meta name="twitter:card" content="summary_large_image"><link rel="preconnect" href="https://play-lh.googleusercontent.com" crossorigin><link rel="stylesheet" href="{BASE}/assets/style.css"><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head><body data-page-section="{e(tail.split("/")[0] if tail else "home")}"><a class="skip-link" href="#main-content">{"تجاوز إلى المحتوى الرئيسي" if lang == "ar" else "Skip to main content"} </a>{nav(lang)}<main id="main-content">{content}</main><footer><span>© DevImpact · FRUIT FURY SLICE</span><span><a href="{e(APP["privacy_policy_url"])}">{"سياسة الخصوصية" if lang == "ar" else "Privacy policy"}</a> · <a href="mailto:{e(APP["support_email"])}">{"الدعم" if lang == "ar" else "Support"}</a></span></footer></body></html>'''

def blog(lang):
    title = "Fruit Fury Slice gameplay blog and guides" if lang == "en" else "مدونة ودلائل اللعب في Fruit Fury Slice"
    desc = "Tips and guides for fruit slicing, combo chains, bomb avoidance and game progression." if lang == "en" else "نصائح وأدلة لتقطيع الفواكه وسلاسل الكومبو وتجنب القنابل والتقدم في اللعبة."
    cards = []
    for slug, et, at, ed, ad, _ in DATA:
        heading, summary = (et, ed) if lang == "en" else (at, ad)
        cards.append(f'<article class="item"><h2><a href="{route_url(lang, "blog/" + slug)}">{e(heading)}</a></h2><p>{e(summary)}</p><a href="{route_url(lang, "blog/" + slug)}">{"Read guide" if lang == "en" else "اقرأ الدليل"}</a></article>')
    content = f'<section class="section"><div class="tag">FRUIT FURY SLICE · {"GAMEPLAY RESOURCES" if lang == "en" else "موارد اللعب"}</div><h1>{e(title)}</h1><p class="lead">{e(desc)}</p><div class="grid">{"".join(cards)}</div></section>'
    return page(lang, "blog", title, desc, content)

def article(lang, item):
    slug, et, at, ed, ad, sections = item
    title, desc = (et, ed) if lang == "en" else (at, ad)
    blocks = "".join(f'<section class="article-section"><h2>{e(h_en if lang == "en" else h_ar)}</h2><p>{e(p_en if lang == "en" else p_ar)}</p></section>' for h_en, h_ar, p_en, p_ar in sections)
    cta = "Play Fruit Fury Slice" if lang == "en" else "العب Fruit Fury Slice"
    content = f'<article class="section article"><h1>{e(title)}</h1><p class="lead">{e(desc)}</p>{blocks}<p><a href="{route_url(lang, "blog")}">{"← All gameplay guides" if lang == "en" else "← جميع أدلة اللعب"}</a></p><div class="end"><h2>{cta}</h2><p>{"Put your timing and precision to the test." if lang == "en" else "اختبر توقيتك ودقتك."}</p><a class="btn" href="{PLAY}" target="_blank" rel="noopener noreferrer">{"Open on Google Play" if lang == "en" else "افتح على Google Play"}</a></div></article>'
    return page(lang, "blog/" + slug, title, desc, content, "Article")

def guide(lang, slug, data):
    et, at, ed, ad, steps = data
    title, desc = (et, ed) if lang == "en" else (at, ad)
    blocks = []
    for i, (h_en, h_ar, p_en, p_ar) in enumerate(steps):
        shot = SHOTS[min(i, len(SHOTS) - 1)]
        image = f'<figure class="guide-shot"><img src="{e(shot["src"])}" width="526" height="296" alt="{e(shot["alt"][lang])}" loading="lazy" decoding="async"><figcaption>{e(shot["caption"][lang])}</figcaption></figure>'
        blocks.append(f'<section class="guide-step"><div class="num">{i+1:02d}</div><div><h2>{e(h_en if lang == "en" else h_ar)}</h2><p>{e(p_en if lang == "en" else p_ar)}</p>{image}</div></section>')
    content = f'<section class="section"><div class="tag">FRUIT FURY SLICE · {"GAME GUIDE" if lang == "en" else "دليل اللعبة"}</div><h1>{e(title)}</h1><p class="lead">{e(desc)}</p><div class="guide-list">{"".join(blocks)}</div></section>'
    return page(lang, slug, title, desc, content)

def feature_page(lang, feature):
    slug = feature["id"]
    index = next(i for i, value in enumerate(FEATURES) if value["id"] == slug)
    title = feature["title"][lang] + " | Fruit Fury Slice"
    desc = feature["description"][lang]
    shot = SHOTS[index]
    sections = "".join(f'<section class="article-section"><h2>{e(h_en if lang == "en" else h_ar)}</h2><p>{e(p_en if lang == "en" else p_ar)}</p></section>' for h_en, h_ar, p_en, p_ar in FEATURE_DETAILS[slug])
    content = f'<article class="section article"><div class="tag">FRUIT FURY SLICE · {"GAME FEATURE" if lang == "en" else "ميزة في اللعبة"}</div><h1>{e(feature["title"][lang])}</h1><p class="lead">{e(desc)}</p><figure class="guide-shot"><img src="{e(shot["src"])}" width="526" height="296" alt="{e(shot["alt"][lang])}" loading="lazy" decoding="async"><figcaption>{e(shot["caption"][lang])}</figcaption></figure>{sections}<p><a href="{route_url(lang, "features")}">{"Explore all features" if lang == "en" else "استكشف جميع المزايا"}</a></p><a class="btn" href="{PLAY}" target="_blank" rel="noopener noreferrer">{"Play on Google Play" if lang == "en" else "العب على Google Play"}</a></article>'
    return page(lang, "features/" + slug, title, desc, content)

def build_extra_pages():
    css = DIST / "assets/style.css"
    css.write_text(css.read_text(encoding="utf-8") + """
.article{max-width:850px;margin:auto}.article h1{font-size:clamp(2.1rem,5vw,3.5rem);line-height:1.2}.article-section{padding:18px 0;border-bottom:1px solid #ffffff18}.article-section h2{font-size:1.45rem}.article-section p,.guide-step p{color:#c1ccda}.guide-list{display:grid;gap:18px;margin-top:28px}.guide-step{display:grid;grid-template-columns:54px 1fr;gap:16px;padding:22px;background:#111925;border:1px solid #283449;border-radius:16px}.guide-step>.num{font-size:1.4rem}.guide-step h2{margin:0 0 8px}.guide-shot{margin:18px 0 0;padding:12px;background:#080b12;border-radius:12px}.guide-shot img{display:block;width:100%;height:auto;object-fit:contain}.guide-shot figcaption{color:#aab6c8;padding-top:8px}.article .end{margin-top:38px}.item a{color:#00c4df}.item h2{font-size:1.3rem;line-height:1.4}nav{align-items:center;gap:10px}.nav-menu{position:relative}.nav-menu>summary{list-style:none;cursor:pointer;display:flex;align-items:center;min-height:44px;padding:8px 13px;border:1px solid #34445c;border-radius:9px;background:#111925;color:#e5edf7;font-weight:700;white-space:nowrap}.nav-menu>summary::-webkit-details-marker{display:none}.nav-menu>summary::after{content:"▾";margin-inline-start:9px;color:#00c4df;font-size:.85em}.nav-menu>summary:focus-visible{outline:3px solid #00c4df;outline-offset:3px}.nav-menu[open]>summary{border-color:#00c4df}.nav-dropdown{position:absolute;top:calc(100% + 8px);inset-inline-start:0;z-index:60;display:grid;gap:3px;width:min(260px,calc(100vw - 36px));padding:8px;background:#111925;border:1px solid #34445c;border-radius:12px;box-shadow:0 16px 36px #0009}.nav-dropdown a{display:flex;align-items:center;min-height:42px;padding:8px 12px;border-radius:8px;color:#dce5f2;text-decoration:none}.nav-dropdown a:hover,.nav-dropdown a:focus-visible{background:#1c2b3e;color:#fff}.nav-dropdown a:focus-visible{outline:2px solid #00c4df;outline-offset:1px}@media(max-width:760px){nav{width:100%;gap:8px}.nav-menu>summary{padding:8px 10px}.nav-dropdown{max-width:calc(100vw - 36px)}.guide-step{grid-template-columns:36px 1fr;padding:16px}}
""", encoding="utf-8")
    for lang in ("en", "ar"):
        for file in (DIST / lang).rglob("index.html"):
            source = file.read_text(encoding="utf-8")
            if "<nav " in source and 'data-nav-group="resources"' not in source:
                extra = '<details class="nav-menu" data-nav-group="resources"><summary>' + ("Gameplay" if lang == "en" else "اللعب") + '</summary><div class="nav-dropdown">'
                labels = [("tips", "Tips" if lang == "en" else "نصائح اللعب"), ("blog", "Blog" if lang == "en" else "المدونة"), ("guide", "Game guide" if lang == "en" else "دليل اللعبة"), ("comparison", "Gameplay" if lang == "en" else "تجربة اللعب")]
                extra += "".join(f'<a data-nav-item="{key}" href="{route_url(lang, key)}">{label}</a>' for key, label in labels) + '</div></details>'
                file.write_text(source.replace("</nav>", extra + "</nav>"), encoding="utf-8")
        p = DIST / lang / "blog" / "index.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(blog(lang), encoding="utf-8")
        for item in DATA:
            p = DIST / lang / "blog" / item[0] / "index.html"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(article(lang, item), encoding="utf-8")
        for slug, data in GUIDES.items():
            p = DIST / lang / slug / "index.html"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(guide(lang, slug, data), encoding="utf-8")
        for feature in FEATURES:
            p = DIST / lang / "features" / feature["id"] / "index.html"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(feature_page(lang, feature), encoding="utf-8")

    entries = [(f"{BASE}/", None)] + [(route_url(lang, tail), tail) for lang, tail in routes()]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    for loc, tail in entries:
        en = f"{BASE}/" if tail is None else route_url("en", tail)
        ar = f"{BASE}/" if tail is None else route_url("ar", tail)
        default = f"{BASE}/" if tail is None else en
        sitemap += f'<url><loc>{e(loc)}</loc><xhtml:link rel="alternate" hreflang="en" href="{e(en)}"/><xhtml:link rel="alternate" hreflang="ar" href="{e(ar)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{e(default)}"/></url>'
    (DIST / "sitemap.xml").write_text(sitemap + "</urlset>", encoding="utf-8")
    (DIST / "sitemap.txt").write_text("\n".join(loc for loc, _ in entries) + "\n", encoding="utf-8")
    llms_path = DIST / "llms.txt"
    llms = llms_path.read_text(encoding="utf-8") + "\n## Fruit Fury Slice gameplay resources\n"
    for lang in ("en", "ar"):
        llms += f"- {lang} blog: {route_url(lang, 'blog')}\n"
        for slug in GUIDES:
            llms += f"- {lang} {slug}: {route_url(lang, slug)}\n"
        for feature in FEATURES:
            llms += f"- {lang} feature {feature['id']}: {route_url(lang, 'features/' + feature['id'])}\n"
    llms_path.write_text(llms, encoding="utf-8")

if __name__ == "__main__":
    build_extra_pages()
