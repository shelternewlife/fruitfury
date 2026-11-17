import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class FruitFuryContentTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "content" / name).read_text(encoding="utf-8"))

    def test_app_identity_and_links(self):
        app = self.load("app.json")
        self.assertEqual(app["name"], "Fruit Fury Slice")
        self.assertEqual(app["package_id"], "com.game.fruitfury.devimpact")
        self.assertEqual(app["google_play_url"], "https://play.google.com/store/apps/details?id=com.game.fruitfury.devimpact")
        self.assertEqual(app["website_url"], "https://shelternewlife.github.io/fruitfury/")
        self.assertEqual(app["category"], "Arcade")

    def test_game_features_and_faq(self):
        features = self.load("features.json")
        faq = self.load("faq.json")
        self.assertEqual(len(features), 4)
        self.assertEqual(len(faq), 12)
        self.assertTrue(all("en" in item["title"] and "ar" in item["title"] for item in features))
        self.assertTrue(all("en" in item["q"] and "ar" in item["q"] for item in faq))

    def test_screenshots_are_from_google_play(self):
        shots = self.load("screenshots.json")
        self.assertEqual(len(shots), 4)
        for shot in shots:
            self.assertTrue(shot["src"].startswith("https://play-lh.googleusercontent.com/"))
            self.assertTrue(shot["alt"]["en"])
            self.assertTrue(shot["alt"]["ar"])

    def test_no_legacy_job_brand_in_active_content(self):
        paths = [
            ROOT / "content" / "app.json",
            ROOT / "content" / "features.json",
            ROOT / "content" / "faq.json",
            ROOT / "content" / "screenshots.json",
            ROOT / "content" / "seo-keywords.json",
            ROOT / "scripts" / "build.py",
            ROOT / "scripts" / "build_resources.py",
            ROOT / "scripts" / "build_locale_resources.py",
        ]
        for path in paths:
            source = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("job connect", source, str(path))
            self.assertNotIn("job search", source, str(path))

    def test_published_locales_have_game_content(self):
        strategy = self.load("market-strategy.json")
        self.assertEqual(
            strategy["published_locales"],
            ["en-US", "en-CA", "fr-CA", "es-ES", "pt-PT", "fr-FR", "de-DE", "it-IT"],
        )
        locales = self.load("locales.json")
        for locale in strategy["published_locales"]:
            self.assertIn(locale, locales)
            if locale not in ("en-US", "en-CA"):
                self.assertEqual(len(locales[locale].get("features", [])), 4)
                self.assertEqual(len(locales[locale].get("faq", [])), 12)
                self.assertEqual(len(locales[locale].get("screenshots", [])), 4)

if __name__ == "__main__":
    unittest.main()
