import requests

payload = { 'api_key': '2cf29d008f842c7e7a150d45394330a1', 'url': 'https://astrogames06.github.io/index.html', 'retry_404': 'true', 'autoparse': 'true', 'country_code': 'eu', 'device_type': 'desktop', 'max_cost': '20', 'session_number': '4' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
