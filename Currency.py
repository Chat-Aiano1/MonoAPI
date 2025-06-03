import os
import requests
import json
import platform

os_name = platform.system()

if os_name == "Windows":
    print("🪟 Windows OS")
    os.system("cls")
elif os_name == "Linux":
    print("🐧 Linux OS")
    os.system("clear")


url = "https://api.monobank.ua/bank/currency"
filename = "monobank_rates.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Дані збережено у файл '{filename}' Для того щоб вийти натисніть 2 рази CTRL+C")

    with open(filename, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)

    USD = 840
    EUR = 978
    UAH = 980

    usd_rate = None
    eur_rate = None

    for rate in saved_data:
        if rate['currencyCodeA'] == USD and rate['currencyCodeB'] == UAH:
            usd_rate = rate
        elif rate['currencyCodeA'] == EUR and rate['currencyCodeB'] == UAH:
            eur_rate = rate

    if usd_rate:
        print("\n💵 Курс USD (Долар) → UAH (Гривня):")
        print(f"Купівля: {usd_rate.get('rateBuy', 'н/д')}")
        print(f"Продаж:  {usd_rate.get('rateSell', 'н/д')}")

    if eur_rate:
        print("\n💶 Курс EUR (Євро) → UAH (Гривня):")
        print(f"Купівля: {eur_rate.get('rateBuy', 'н/д')}")
        print(f"Продаж:  {eur_rate.get('rateSell', 'н/д')}")
        os.system("cat")
        os.system("clear")

    if not usd_rate and not eur_rate:
        print("❌ Не знайдено курсів для USD та EUR.")

    if os_name == "Linux":
        os.system(f"cat")
        os.system(f"clear")

except requests.exceptions.RequestException as e:
    print(f"🔴 Помилка HTTP-запиту: {e}")
except (ValueError, json.JSONDecodeError):
    print("🔴 Помилка обробки JSON.")
except IOError as e:
    print(f"🔴 Помилка при роботі з файлом: {e}")

