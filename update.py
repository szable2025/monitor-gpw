import json
from datetime import datetime

# Na razie dane przykładowe - później zastąp je danymi z internetu
companies_data = [
    {"name": "Spółka A", "ticker": "SPA", "pe_ratio": 10.5, "pb_ratio": 1.2, "dcf_valuation": 50},
    {"name": "Spółka B", "ticker": "SPB", "pe_ratio": 14.8, "pb_ratio": 1.6, "dcf_valuation": 42.3},
    {"name": "Spółka C", "ticker": "SPC", "pe_ratio": 9.3, "pb_ratio": 0.9, "dcf_valuation": 35}
]

data = {
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "companies": companies_data
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
