import requests
import json

my_currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{my_currency}.json")
rates = json.loads(r.content)
if my_currency == "usd":
    ex_rate = {"eur": rates["eur"]["rate"]}
elif my_currency == "eur":
    ex_rate = {"usd": rates["usd"]["rate"]}
else:
    ex_rate = {"usd": rates["usd"]["rate"], "eur": rates["eur"]["rate"]}
while True:
    target_currency = input().lower()
    if target_currency:
        amount = float(input())
        print("Checking the cache...")
        if target_currency not in ex_rate:
            ex_rate[target_currency] = rates[target_currency]["rate"]
            print("Sorry, but it is not in the cache!")
        else:
            print("Oh! It is in the cache!")
        received_amount = round(amount * ex_rate[target_currency], 2)
        print(f"You received {received_amount} {target_currency.upper()}.")
    else:
        break
