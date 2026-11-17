#!/usr/bin/env python3
"""Generate localized Fruit Fury Slice gameplay resource hubs."""
import html
import json
import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
APP = json.loads((ROOT / "content/app.json").read_text(encoding="utf-8"))
STRATEGY = json.loads((ROOT / "content/market-strategy.json").read_text(encoding="utf-8"))
BASE = APP["website_url"].rstrip("/")
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML = "http://www.w3.org/1999/xhtml"
HUBS = ("tips", "blog", "guide", "comparison")

CONTENT = {
 "en-US": {
  "language_name":"US English","nav":{"tips":"Tips","blog":"Blog","guide":"Game guide","comparison":"Gameplay"},
  "labels":{"skip":"Skip to main content","resource":"GAMEPLAY RESOURCES","home":"Back to the home page","privacy":"Privacy policy","support":"Support","more":"Read guide","nav_aria":"Primary navigation"},
  "pages":{
   "tips":("Fruit Fury Slice tips | Slice, combo and dodge","Practical tips for timing, precision and safer fruit-slicing runs.","Gameplay tips","Build cleaner swipes, extend combo chains and stay alert for bombs.",[("Slice with precision","Use controlled swipes and watch the movement of fruit before you cut.","guide"),("Build combo chains","Slice multiple fruits in quick succession while keeping control.","blog"),("Avoid bombs","Check the play area before each move and never chase a combo blindly.","comparison")]),
   "blog":("Fruit Fury Slice blog and gameplay guides","Guides about fruit slicing, combo chains, bombs, levels and rewards.","Fruit Fury Slice gameplay resources","Explore practical guides that explain the game's core arcade loop.",[("Precision slicing","Improve timing and accuracy with deliberate swipes.","tips"),("Combo strategy","Understand rhythm, streaks and score improvement.","guide"),("Bomb awareness","Learn safer decisions when fruit and hazards appear together.","comparison")]),
   "guide":("Fruit Fury Slice user guide | Android arcade game","A walkthrough of the home screen, gameplay, rewards and settings.","Fruit Fury Slice game guide","Follow the main screens and learn what to look for during a run.",[("Home screen","See your current level, best score, credits, Play, Store and Settings.","tips"),("Gameplay screen","Follow score, coins, level, combo and timer or target indicators.","blog"),("Store and settings","Review the Run Support Store, haptic feedback, privacy and support.","comparison")]),
   "comparison":("Fruit Fury Slice gameplay | Quick arcade sessions","What makes the game easy to start and challenging to master.","A focused arcade experience","Explore the core loop: simple swipes, precise timing, hazards and rising challenge.",[("Easy to understand","Swipe to slice fruit as it appears on screen.","guide"),("Skill develops with practice","Improve timing, accuracy and awareness of bombs.","tips"),("Play offline","The Google Play description says the core arcade experience supports offline play.","blog")])
  }
 },
 "en-CA": {
  "language_name":"English (Canada)","nav":{"tips":"Tips","blog":"Blog","guide":"Game guide","comparison":"Gameplay"},
  "labels":{"skip":"Skip to main content","resource":"GAMEPLAY RESOURCES","home":"Back to the home page","privacy":"Privacy policy","support":"Support","more":"Read guide","nav_aria":"Primary navigation"},
  "pages":{
   "tips":("Fruit Fury Slice tips | Slice, combo and dodge","Practical tips for timing, precision and safer fruit-slicing runs.","Gameplay tips","Build cleaner swipes, extend combo chains and stay alert for bombs.",[("Slice with precision","Use controlled swipes and watch the movement of fruit before you cut.","guide"),("Build combo chains","Slice multiple fruits in quick succession while keeping control.","blog"),("Avoid bombs","Check the play area before each move and never chase a combo blindly.","comparison")]),
   "blog":("Fruit Fury Slice blog and gameplay guides","Guides about fruit slicing, combo chains, bombs, levels and rewards.","Fruit Fury Slice gameplay resources","Explore practical guides that explain the game's core arcade loop.",[("Precision slicing","Improve timing and accuracy with deliberate swipes.","tips"),("Combo strategy","Understand rhythm, streaks and score improvement.","guide"),("Bomb awareness","Learn safer decisions when fruit and hazards appear together.","comparison")]),
   "guide":("Fruit Fury Slice user guide | Android arcade game","A walkthrough of the home screen, gameplay, rewards and settings.","Fruit Fury Slice game guide","Follow the main screens and learn what to look for during a run.",[("Home screen","See your current level, best score, credits, Play, Store and Settings.","tips"),("Gameplay screen","Follow score, coins, level, combo and timer or target indicators.","blog"),("Store and settings","Review the Run Support Store, haptic feedback, privacy and support.","comparison")]),
   "comparison":("Fruit Fury Slice gameplay | Quick arcade sessions","What makes the game easy to start and challenging to master.","A focused arcade experience","Explore the core loop: simple swipes, precise timing, hazards and rising challenge.",[("Easy to understand","Swipe to slice fruit as it appears on screen.","guide"),("Skill develops with practice","Improve timing, accuracy and awareness of bombs.","tips"),("Play offline","The Google Play description says the core arcade experience supports offline play.","blog")])
  }
 },
 "fr-CA": {
  "language_name":"Français (Canada)","nav":{"tips":"Conseils","blog":"Blogue","guide":"Guide du jeu","comparison":"Jeu"},
  "labels":{"skip":"Passer au contenu principal","resource":"RESSOURCES DE JEU","home":"Retour à l’accueil","privacy":"Politique de confidentialité","support":"Soutien","more":"Lire le guide","nav_aria":"Navigation principale"},
  "pages":{
   "tips":("Conseils Fruit Fury Slice | Couper, enchaîner et éviter","Des conseils pratiques pour améliorer le rythme, la précision et la sécurité de vos parties.","Conseils de jeu","Effectuez des gestes précis, prolongez les combos et restez attentif aux bombes.",[("Couper avec précision","Effectuez des gestes contrôlés et observez les fruits avant de couper.","guide"),("Créer des combos","Coupez plusieurs fruits rapidement tout en gardant le contrôle.","blog"),("Éviter les bombes","Vérifiez l’écran avant chaque geste et ne poursuivez pas un combo à l’aveugle.","comparison")]),
   "blog":("Blogue et guides de jeu Fruit Fury Slice","Des guides sur les fruits, les combos, les bombes, les niveaux et les récompenses.","Ressources Fruit Fury Slice","Consultez des guides pratiques sur les principales mécaniques du jeu.",[("Coupe précise","Améliorez votre rythme et votre précision.","tips"),("Stratégie de combo","Comprenez le rythme et les séries de coupes.","guide"),("Attention aux bombes","Prenez des décisions plus sûres lorsque fruits et dangers apparaissent ensemble.","comparison")]),
   "guide":("Guide Fruit Fury Slice | Jeu d’arcade Android","Un aperçu de l’écran d’accueil, du jeu, des récompenses et des réglages.","Guide du jeu Fruit Fury Slice","Découvrez les écrans principaux et les éléments à surveiller pendant une partie.",[("Écran d’accueil","Consultez le niveau, le meilleur score, les crédits, Jouer, Boutique et Réglages.","tips"),("Écran de jeu","Suivez le score, les pièces, le niveau, le combo et le chronomètre ou l’objectif.","blog"),("Boutique et réglages","Découvrez la boutique de soutien, le retour haptique, la confidentialité et le soutien.","comparison")]),
   "comparison":("Fruit Fury Slice | Des parties d’arcade rapides","Ce qui rend le jeu facile à commencer et stimulant à maîtriser.","Une expérience d’arcade ciblée","Découvrez les gestes simples, la précision, les dangers et la difficulté progressive.",[("Facile à comprendre","Glissez pour couper les fruits qui apparaissent à l’écran.","guide"),("La pratique développe l’habileté","Améliorez votre rythme, votre précision et votre attention aux bombes.","tips"),("Jouer hors ligne","La description Google Play indique que l’expérience d’arcade principale fonctionne hors ligne.","blog")])
  }
 },
 "es-ES": {
  "language_name":"Español (España)","nav":{"tips":"Consejos","blog":"Blog","guide":"Guía del juego","comparison":"Juego"},
  "labels":{"skip":"Saltar al contenido principal","resource":"RECURSOS DE JUEGO","home":"Volver a la página principal","privacy":"Política de privacidad","support":"Ayuda","more":"Leer guía","nav_aria":"Navegación principal"},
  "pages":{
   "tips":("Consejos de Fruit Fury Slice | Corta, combina y esquiva","Consejos prácticos para mejorar el ritmo, la precisión y la seguridad al jugar.","Consejos de juego","Haz movimientos precisos, encadena combos y mantente alerta ante las bombas.",[("Corta con precisión","Haz movimientos controlados y observa las frutas antes de cortar.","guide"),("Crea cadenas de combo","Corta varias frutas seguidas sin perder el control.","blog"),("Evita las bombas","Revisa la pantalla antes de cada movimiento y no persigas combos a ciegas.","comparison")]),
   "blog":("Blog y guías de juego de Fruit Fury Slice","Guías sobre frutas, combos, bombas, niveles y recompensas.","Recursos de Fruit Fury Slice","Consulta guías prácticas sobre las mecánicas principales del juego.",[("Corte preciso","Mejora el ritmo y la precisión de tus movimientos.","tips"),("Estrategia de combos","Comprende el ritmo y las cadenas de cortes.","guide"),("Atención a las bombas","Toma decisiones más seguras cuando aparecen frutas y peligros juntos.","comparison")]),
   "guide":("Guía de Fruit Fury Slice | Juego arcade para Android","Un recorrido por la pantalla principal, el juego, las recompensas y los ajustes.","Guía del juego Fruit Fury Slice","Conoce las pantallas principales y qué debes observar durante una partida.",[("Pantalla principal","Consulta el nivel, la mejor puntuación, los créditos, Jugar, Tienda y Ajustes.","tips"),("Pantalla de juego","Sigue la puntuación, monedas, nivel, combo y temporizador u objetivo.","blog"),("Tienda y ajustes","Revisa la tienda de apoyo, la respuesta háptica, la privacidad y la ayuda.","comparison")]),
   "comparison":("Fruit Fury Slice | Partidas arcade rápidas","Qué hace que el juego sea fácil de empezar y difícil de dominar.","Una experiencia arcade centrada","Descubre los controles sencillos, la precisión, los peligros y el reto progresivo.",[("Fácil de entender","Desliza para cortar las frutas que aparecen en pantalla.","guide"),("La habilidad mejora con práctica","Mejora el ritmo, la precisión y la atención a las bombas.","tips"),("Juega sin conexión","La descripción de Google Play indica que la experiencia arcade principal admite juego sin conexión.","blog")])
  }
 },
 "pt-PT": {
  "language_name":"Português (Portugal)","nav":{"tips":"Dicas","blog":"Blogue","guide":"Guia do jogo","comparison":"Jogo"},
  "labels":{"skip":"Saltar para o conteúdo principal","resource":"RECURSOS DE JOGO","home":"Voltar à página inicial","privacy":"Política de privacidade","support":"Apoio","more":"Ler guia","nav_aria":"Navegação principal"},
  "pages":{
   "tips":("Dicas Fruit Fury Slice | Cortar, combinar e evitar","Dicas práticas para melhorar o ritmo, a precisão e a segurança durante o jogo.","Dicas de jogo","Faça movimentos precisos, crie combos e mantenha-se atento às bombas.",[("Corte com precisão","Faça movimentos controlados e observe os frutos antes de cortar.","guide"),("Crie cadeias de combo","Corte vários frutos em sequência sem perder o controlo.","blog"),("Evite as bombas","Observe o ecrã antes de cada movimento e não persiga combos às cegas.","comparison")]),
   "blog":("Blogue e guias de jogo Fruit Fury Slice","Guias sobre frutos, combos, bombas, níveis e recompensas.","Recursos Fruit Fury Slice","Consulte guias práticos sobre as principais mecânicas do jogo.",[("Corte preciso","Melhore o ritmo e a precisão dos movimentos.","tips"),("Estratégia de combos","Compreenda o ritmo e as sequências de cortes.","guide"),("Atenção às bombas","Tome decisões mais seguras quando surgem frutos e perigos em simultâneo.","comparison")]),
   "guide":("Guia Fruit Fury Slice | Jogo arcade para Android","Uma visão do ecrã inicial, da jogabilidade, das recompensas e das definições.","Guia do jogo Fruit Fury Slice","Conheça os ecrãs principais e o que deve observar durante uma partida.",[("Ecrã inicial","Consulte o nível, a melhor pontuação, os créditos, Jogar, Loja e Definições.","tips"),("Ecrã de jogo","Acompanhe a pontuação, moedas, nível, combo e temporizador ou objetivo.","blog"),("Loja e definições","Consulte a loja de apoio, a resposta háptica, a privacidade e o apoio.","comparison")]),
   "comparison":("Fruit Fury Slice | Sessões arcade rápidas","O que torna o jogo fácil de começar e desafiante de dominar.","Uma experiência arcade focada","Explore controlos simples, precisão, perigos e dificuldade progressiva.",[("Fácil de compreender","Deslize para cortar os frutos que aparecem no ecrã.","guide"),("A prática desenvolve a perícia","Melhore o ritmo, a precisão e a atenção às bombas.","tips"),("Jogue offline","A descrição do Google Play indica que a experiência arcade principal permite jogar offline.","blog")])
  }
 },
 "fr-FR": {
  "language_name":"Français (France)","nav":{"tips":"Conseils","blog":"Blog","guide":"Guide du jeu","comparison":"Jeu"},
  "labels":{"skip":"Aller au contenu principal","resource":"RESSOURCES DE JEU","home":"Retour à l’accueil","privacy":"Politique de confidentialité","support":"Assistance","more":"Lire le guide","nav_aria":"Navigation principale"},
  "pages":{
   "tips":("Conseils Fruit Fury Slice | Couper, enchaîner et esquiver","Des conseils pour améliorer le rythme, la précision et la sécurité de vos parties.","Conseils de jeu","Effectuez des gestes précis, enchaînez les combos et restez attentif aux bombes.",[("Couper avec précision","Effectuez des gestes maîtrisés et observez les fruits avant de couper.","guide"),("Créer des combos","Coupez plusieurs fruits rapidement tout en gardant le contrôle.","blog"),("Éviter les bombes","Vérifiez l’écran avant chaque geste et ne poursuivez pas un combo à l’aveugle.","comparison")]),
   "blog":("Blog et guides de jeu Fruit Fury Slice","Des guides sur les fruits, les combos, les bombes, les niveaux et les récompenses.","Ressources Fruit Fury Slice","Découvrez des guides pratiques sur les mécaniques principales du jeu.",[("Coupe précise","Améliorez votre rythme et votre précision.","tips"),("Stratégie de combo","Comprenez le rythme et les séries de coupes.","guide"),("Attention aux bombes","Faites des choix plus sûrs lorsque fruits et dangers apparaissent ensemble.","comparison")]),
   "guide":("Guide Fruit Fury Slice | Jeu d’arcade Android","Un aperçu de l’accueil, du jeu, des récompenses et des paramètres.","Guide du jeu Fruit Fury Slice","Découvrez les écrans principaux et les éléments à surveiller pendant une partie.",[("Écran d’accueil","Consultez le niveau, le meilleur score, les crédits, Jouer, Boutique et Paramètres.","tips"),("Écran de jeu","Suivez le score, les pièces, le niveau, le combo et le chronomètre ou l’objectif.","blog"),("Boutique et paramètres","Consultez la boutique de soutien, le retour haptique, la confidentialité et l’assistance.","comparison")]),
   "comparison":("Fruit Fury Slice | Des parties d’arcade rapides","Pourquoi le jeu est facile à commencer et stimulant à maîtriser.","Une expérience d’arcade ciblée","Découvrez les gestes simples, la précision, les dangers et la difficulté progressive.",[("Facile à comprendre","Faites glisser votre doigt pour couper les fruits à l’écran.","guide"),("La pratique développe l’adresse","Améliorez votre rythme, votre précision et votre attention aux bombes.","tips"),("Jouer hors ligne","La description Google Play indique que l’expérience d’arcade principale fonctionne hors ligne.","blog")])
  }
 },
 "de-DE": {
  "language_name":"Deutsch (Deutschland)","nav":{"tips":"Tipps","blog":"Blog","guide":"Spielanleitung","comparison":"Gameplay"},
  "labels":{"skip":"Zum Hauptinhalt springen","resource":"SPIELTIPPS","home":"Zur Startseite","privacy":"Datenschutzerklärung","support":"Support","more":"Anleitung lesen","nav_aria":"Hauptnavigation"},
  "pages":{
   "tips":("Fruit Fury Slice Tipps | Schneiden, Kombos und Ausweichen","Praktische Tipps für Timing, Präzision und sichere Frucht-Slicing-Runden.","Gameplay-Tipps","Setze präzise Wischbewegungen ein, bilde Kombos und achte auf Bomben.",[("Präzise schneiden","Wische kontrolliert und beobachte die Früchte, bevor du schneidest.","guide"),("Kombos aufbauen","Schneide mehrere Früchte schnell hintereinander und behalte die Kontrolle.","blog"),("Bomben vermeiden","Prüfe das Spielfeld vor jeder Bewegung und erzwinge keine Combo.","comparison")]),
   "blog":("Fruit Fury Slice Blog und Gameplay-Anleitungen","Anleitungen zu Früchten, Kombos, Bomben, Leveln und Belohnungen.","Fruit Fury Slice Spielressourcen","Entdecke praktische Anleitungen zu den wichtigsten Spielmechaniken.",[("Präzises Schneiden","Verbessere Timing und Genauigkeit deiner Wischbewegungen.","tips"),("Combo-Strategie","Verstehe Rhythmus, Serien und Punkteverbesserung.","guide"),("Auf Bomben achten","Triff sichere Entscheidungen, wenn Früchte und Gefahren zusammen erscheinen.","comparison")]),
   "guide":("Fruit Fury Slice Anleitung | Android-Arcade-Spiel","Ein Überblick über Startbildschirm, Gameplay, Belohnungen und Einstellungen.","Fruit Fury Slice Spielanleitung","Lerne die wichtigsten Bildschirme und Anzeigen während einer Runde kennen.",[("Startbildschirm","Sieh aktuelles Level, Bestwert, Guthaben sowie Spielen, Store und Einstellungen.","tips"),("Gameplay-Bildschirm","Behalte Punktzahl, Münzen, Level, Combo und Timer oder Ziel im Blick.","blog"),("Store und Einstellungen","Sieh dir Run Support Store, haptisches Feedback, Datenschutz und Support an.","comparison")]),
   "comparison":("Fruit Fury Slice | Kurze Arcade-Runden","Was das Spiel leicht zugänglich und zugleich anspruchsvoll macht.","Ein fokussiertes Arcade-Erlebnis","Entdecke einfache Steuerung, Präzision, Gefahren und steigenden Schwierigkeitsgrad.",[("Leicht zu verstehen","Wische, um Früchte zu schneiden, sobald sie erscheinen.","guide"),("Übung verbessert deine Fähigkeiten","Verbessere Timing, Genauigkeit und Aufmerksamkeit für Bomben.","tips"),("Offline spielen","Laut Google-Play-Beschreibung unterstützt das zentrale Arcade-Erlebnis Offline-Spiel.","blog")])
  }
 },
 "it-IT": {
  "language_name":"Italiano (Italia)","nav":{"tips":"Consigli","blog":"Blog","guide":"Guida al gioco","comparison":"Gameplay"},
  "labels":{"skip":"Vai al contenuto principale","resource":"RISORSE DI GIOCO","home":"Torna alla home","privacy":"Informativa sulla privacy","support":"Assistenza","more":"Leggi la guida","nav_aria":"Navigazione principale"},
  "pages":{
   "tips":("Consigli Fruit Fury Slice | Taglia, combina ed evita","Consigli pratici per migliorare tempismo, precisione e sicurezza durante le partite.","Consigli di gioco","Usa swipe precisi, crea combo e fai attenzione alle bombe.",[("Taglia con precisione","Esegui swipe controllati e osserva i frutti prima di tagliare.","guide"),("Crea catene combo","Taglia più frutti in rapida successione mantenendo il controllo.","blog"),("Evita le bombe","Controlla l’area di gioco prima di ogni movimento e non inseguire combo alla cieca.","comparison")]),
   "blog":("Blog e guide di gioco Fruit Fury Slice","Guide su frutta, combo, bombe, livelli e ricompense.","Risorse Fruit Fury Slice","Scopri guide pratiche sulle meccaniche principali del gioco.",[("Taglio preciso","Migliora tempismo e precisione degli swipe.","tips"),("Strategia combo","Comprendi ritmo, sequenze e miglioramento del punteggio.","guide"),("Attenzione alle bombe","Scegli con prudenza quando frutti e pericoli appaiono insieme.","comparison")]),
   "guide":("Guida Fruit Fury Slice | Gioco arcade Android","Una panoramica della schermata iniziale, del gioco, delle ricompense e delle impostazioni.","Guida al gioco Fruit Fury Slice","Scopri le schermate principali e cosa osservare durante una partita.",[("Schermata iniziale","Visualizza livello attuale, record, crediti, Gioca, Store e Impostazioni.","tips"),("Schermata di gioco","Segui punteggio, monete, livello, combo e timer o obiettivo.","blog"),("Store e impostazioni","Consulta Run Support Store, feedback aptico, privacy e assistenza.","comparison")]),
   "comparison":("Fruit Fury Slice | Sessioni arcade rapide","Cosa rende il gioco semplice da iniziare e stimolante da padroneggiare.","Un’esperienza arcade mirata","Scopri comandi semplici, precisione, pericoli e difficoltà progressiva.",[("Facile da capire","Scorri per tagliare i frutti quando appaiono sullo schermo.","guide"),("L’abilità cresce con la pratica","Migliora tempismo, precisione e attenzione alle bombe.","tips"),("Gioca offline","La descrizione Google Play indica che l’esperienza arcade principale supporta il gioco offline.","blog")])
  }
 }
}

def esc(value):
    return html.escape(str(value), quote=True)

def route(locale, tail):
    return f"{BASE}/{locale.lower()}/{tail}/"

def render_page(locale, tail):
    data = CONTENT[locale]
    title, description, heading, intro, cards = data["pages"][tail]
    labels = data["labels"]
    import build
    flags = build.render_market_flags(tail, locale)
    primary = build.TEXT["en"]
    nav_primary = [
        ("about", primary["about"]), ("features", primary["features"]),
        ("download", primary["download_nav"]), ("faq", primary["faq"])
    ]
    primary_links = "".join(f'<a data-nav-item="{key}" href="{BASE}/{locale.lower()}/{key}/">{esc(label)}</a>' for key, label in nav_primary)
    resource_links = "".join(f'<a data-nav-item="{key}" href="{route(locale, key)}">{esc(data["nav"][key])}</a>' for key in HUBS)
    nav_groups = {
      "en-US":("Explore","Gameplay"),"en-CA":("Explore","Gameplay"),
      "fr-CA":("Explorer","Jeu"),"fr-FR":("Explorer","Jeu"),
      "es-ES":("Explorar","Juego"),"pt-PT":("Explorar","Jogo"),
      "de-DE":("Entdecken","Spiel"),"it-IT":("Esplora","Gioco")
    }
    groups = nav_groups[locale]
    nav = f'<details class="nav-menu" data-nav-group="primary"><summary>{groups[0]}</summary><div class="nav-dropdown">{primary_links}</div></details><details class="nav-menu" data-nav-group="resources"><summary>{groups[1]}</summary><div class="nav-dropdown">{resource_links}</div></details>'
    cards_html = "".join(f'<article class="item"><h2><a href="{route(locale, target)}">{esc(card_title)}</a></h2><p>{esc(card_text)}</p><a href="{route(locale, target)}">{esc(labels["more"])}</a></article>' for card_title, card_text, target in cards)
    alternates = "".join(f'<link rel="alternate" hreflang="{code}" href="{route(code, tail)}">' for code in STRATEGY["published_locales"])
    alternates += f'<link rel="alternate" hreflang="x-default" href="{route("en-US", tail)}">'
    organization = {"@type":"Organization","@id":f"{BASE}/#organization","name":APP["developer"],"url":BASE+"/","email":APP["support_email"]}
    schema = {"@context":"https://schema.org","@graph":[organization,{"@type":"WebPage","name":title,"description":description,"url":route(locale,tail),"inLanguage":locale,"publisher":{"@id":f"{BASE}/#organization"}}]}
    return f'''<!doctype html><html lang="{locale}" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{route(locale,tail)}">{alternates}<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{route(locale,tail)}"><meta property="og:image" content="{esc(json.loads((ROOT / "content/screenshots.json").read_text(encoding="utf-8"))[0]["src"])}"><meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="{BASE}/assets/style.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body data-page-section="{tail}"><a class="skip-link" href="#main-content">{esc(labels["skip"])}</a><header class="standard-header">{flags}<div class="header-main"><a class="brand" href="{BASE}/">FRUIT <b>FURY</b></a><nav aria-label="{esc(labels["nav_aria"])}">{nav}</nav></div></header><main id="main-content"><section class="section"><div class="tag">FRUIT FURY SLICE · {esc(labels["resource"])}</div><h1>{esc(heading)}</h1><p class="lead">{esc(intro)}</p><div class="grid">{cards_html}</div><div class="end"><h2>Fruit Fury Slice</h2><p>{esc(APP["tagline"]["en"])}</p><a class="btn" href="{APP["google_play_url"]}" target="_blank" rel="noopener noreferrer">Google Play</a></div></section></main><footer><span>© DevImpact · FRUIT FURY SLICE</span><span><a href="{esc(APP["privacy_policy_url"])}">{esc(labels["privacy"])}</a> · <a href="mailto:{esc(APP["support_email"])}">{esc(labels["support"])}</a></span></footer></body></html>'''

def build_localized_resource_pages():
    published = STRATEGY["published_locales"]
    for locale in published:
        for tail in HUBS:
            path = DIST / locale.lower() / tail / "index.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_page(locale, tail), encoding="utf-8")

    sitemap_path = DIST / "sitemap.xml"
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ET.register_namespace("", NS)
    ET.register_namespace("xhtml", XHTML)
    for locale in published:
        for tail in HUBS:
            loc = route(locale, tail)
            existing = next((node for node in root.findall(f"{{{NS}}}url") if node.findtext(f"{{{NS}}}loc") == loc), None)
            if existing is not None:
                root.remove(existing)
            node = ET.SubElement(root, f"{{{NS}}}url")
            ET.SubElement(node, f"{{{NS}}}loc").text = loc
            for code in published:
                ET.SubElement(node, f"{{{XHTML}}}link", {"rel":"alternate","hreflang":code,"href":route(code,tail)})
            ET.SubElement(node, f"{{{XHTML}}}link", {"rel":"alternate","hreflang":"x-default","href":route("en-US",tail)})
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

    text_path = DIST / "sitemap.txt"
    urls = [line.strip() for line in text_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    for locale in published:
        for tail in HUBS:
            loc = route(locale, tail)
            if loc not in urls:
                urls.append(loc)
    text_path.write_text("\n".join(urls) + "\n", encoding="utf-8")

    llms_path = DIST / "llms.txt"
    llms = llms_path.read_text(encoding="utf-8") + "\n## Localized Fruit Fury Slice gameplay resources\n"
    for locale in published:
        for tail in HUBS:
            llms += f"- {locale} {tail}: {route(locale,tail)}\n"
    llms_path.write_text(llms, encoding="utf-8")

if __name__ == "__main__":
    build_localized_resource_pages()
