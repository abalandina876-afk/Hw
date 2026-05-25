import requests
from bs4 import BeautifulSoup


class CurrencyConverter:

    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://bank.gov.ua/ua/markets/exchangerates"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Шукаємо рядок з USD
        rows = soup.find_all("tr")

        for row in rows:
            columns = row.find_all("td")

            if len(columns) > 4:
                currency = columns[1].text.strip()

                if currency == "USD":
                    rate = columns[4].text.strip().replace(",", ".")
                    return float(rate)

        return None

    def convert_uah_to_usd(self, amount_uah):
        return amount_uah / self.usd_rate

converter = CurrencyConverter()

if converter.usd_rate:
    print("Курс долара:", converter.usd_rate)

    amount = float(input("Введіть суму у гривнях: "))

    usd = converter.convert_uah_to_usd(amount)

    print(f"{amount} грн = {usd:.2f} USD")

else:
    print("Не вдалося отримати курс валют.")