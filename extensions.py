import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось определить валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось определить валюту {base}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionException(f'Не удалось определить количество {amount}')

        r = requests.get(
        f'https://api.currencyapi.com/v3/latest?apikey=cur_live_zqAV92DwdaMYmtnjTaHtEMZckaSj7kBvgqPHVWI1&currencies={quote_ticker}&base_currency={base_ticker}')
        total_base = json.loads(r.content)['data'][f'{quote_ticker}']['value']

        return total_base
