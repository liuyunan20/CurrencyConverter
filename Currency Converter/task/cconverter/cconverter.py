import requests
import json

currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
rates = json.loads(r.content)
print(rates["usd"])
print(rates["eur"])
