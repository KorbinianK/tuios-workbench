"""Build index.html from src/template.html and the data files.

Run: python3 build.py
"""
from pathlib import Path

root = Path(__file__).parent
template = (root / "src/template.html").read_text()
options = (root / "data/options.json").read_text().strip()
themes = (root / "data/themes.json").read_text().strip()
assert "</script" not in options and "</script" not in themes
html = template.replace("__OPTS__", options).replace("__THEMES__", themes)
page = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + html + "\n</body>\n</html>\n"
(root / "index.html").write_text(page)
print("wrote index.html")
