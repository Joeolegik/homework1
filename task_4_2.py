import requests
from datetime import datetime


def currency_rates(c_code: object) -> object:
    link = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(link).text
    # print(response)
    idx = response.find('Date')
    date = response[idx + 6:idx + 16]
    date_updated = datetime.date(datetime.strptime(date, "%d.%m.%Y"))
    currencies = []
    for el in response.split('<CharCode>')[1:]:
        currencies.append(el.split("</CharCode>")[0])

    # print(currencies) #['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR',...]
    c_values = []
    for el in response.split('<Value>')[1:]:
        c_values.append(float(el.split('</Value>')[0].replace(',', '.')))
        # c_values.append(Decimal(float(el.split('</Value>')[0].replace(',', '.'))))

    currency_catalog = dict(zip(currencies, c_values))
    # print(currency_catalog)
    c_code = c_code.upper()
    date = date_updated
    currency_result = currency_catalog.get(c_code)
    result = f'Today`s {c_code} is {currency_result} rub.\nDate: {date}'
    return result


if __name__ == "__main__":
    usd = currency_rates('usd')
    eur = currency_rates('EUR')
    print(usd)
    print(eur)
