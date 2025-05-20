import json
import datetime

# Przykładowe dane — zastąp później prawdziwym scrapingiem (np. z Biznesradar)
stocks = [
    {"name": "Spółka A", "ticker": "SPA", "cz": 10.5, "cwk": 1.2, "dcf": 50.0},
    {"name": "Spółka B", "ticker": "SPB", "cz": 14.8, "cwk": 1.6, "dcf": 42.3},
    {"name": "Spółka C", "ticker": "SPC", "cz": 9.3,  "cwk": 0.9, "dcf": 35.0},
]

data = {
    "updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "stocks": stocks
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
