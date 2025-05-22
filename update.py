import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time

companies = [
    {"name": "Asseco Poland", "ticker": "ACP"},
    {"name": "CD Projekt", "ticker": "CDR"},
    {"name": "Dino Polska", "ticker": "DNP"}
]

def get_financial_data(ticker):
    url = f"https://www.biznesradar.pl/notowania/{ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rows = soup.select('table.qTableFull tr')
        data = {}
        for row in rows:
            label = row.select_one('th')
            value = row.select_one('td')
            if label and value:
                label_text = label.text.strip()
                value_text = value.text.strip().replace(',', '.')
                if 'C/Z' in label_text:
                    data["pe_ratio"] = float(value_text)
                if 'C/WK' in label_text:
                    data["pb_ratio"] = float(value_text)
        return data
    except Exception as e:
        print(f"Błąd przy tickerze {ticker}: {e}")
        return {"pe_ratio": None, "pb_ratio": None}

results = []
for c in companies:
    print(f"Pobieranie danych dla {c['ticker']}...")
    data = get_financial_data(c["ticker"])
    results.append({
        "name": c["name"],
        "ticker": c["ticker"],
        "pe_ratio": data.get("pe_ratio"),
        "pb_ratio": data.get("pb_ratio"),
        "dcf_valuation": None  # miejsce na DCF w przyszłości
    })
    time.sleep(2)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "companies": results
    }, f, indent=4, ensure_ascii=False)
