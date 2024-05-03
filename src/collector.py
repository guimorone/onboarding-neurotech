from typing import Dict, Any
from requests import get
from bs4 import BeautifulSoup
from .utils import encode_url
from .constants import *


class Collector:
    def __init__(self, code: str) -> None:
        self.code: str = code
        encoded_code: str = encode_url(code)
        self.url: str = f'{BASE_URL}?p={encoded_code}'

    def collect(self) -> Dict[str, Any]:
        response: Dict[str, Any] = {}
        page = get(self.url)
        soup = BeautifulSoup(page.text, 'xml')
        print('Content:', soup.prettify(), sep='\n')
        products = soup.find_all('prod')

        for product in products:
            code = product.find('cProd').get_text()
            name = product.find('xProd').get_text()
            qtd = product.find('qCom').get_text()
            unit_value = product.find('vUnCom').get_text()
            total_value = product.find('vProd').get_text()

            response[name] = {
                'code': code,
                'qtd': qtd,
                'unit_value': unit_value,
                'total_value': total_value,
            }

        return response
