# Fruit Fury Slice — Game Website

A multilingual static website for **Fruit Fury Slice** by **DevImpact**.

- Google Play: https://play.google.com/store/apps/details?id=com.game.fruitfury.devimpact
- Website: https://shelternewlife.github.io/fruitfury/
- Package ID: `com.game.fruitfury.devimpact`
- Category: Arcade

## Website content

The site describes the published game experience: fruit slicing with touch swipes, combo chains, bomb avoidance, progressive levels, score chasing, coins and gems, and offline play. Screenshots are sourced from the official Google Play listing.

## Build and validation

```bash
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/validate.py
```

GitHub Actions builds the static site and deploys the generated `dist/` directory to GitHub Pages.
