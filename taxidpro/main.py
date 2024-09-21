import requests

BASE_URL = 'https://v3.api.taxid.pro'


class TaxIDPro:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def validate(self, country: str, tin: str, type: str = 'any'):
        res = requests.get(
            f'{BASE_URL}/validate?country={country}&tin={tin}&type={type}',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        res.raise_for_status()
        return res.json()

    def lookup(self, country: str, tin: str, type: str = 'vat'):
        if type != 'vat':
            raise ValueError('lookup type must be vat')
        res = requests.get(
            f'{BASE_URL}/lookup?country={country}&tin={tin}&type={type}',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        res.raise_for_status()
        return res.json()
