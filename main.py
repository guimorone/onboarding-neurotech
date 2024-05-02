from typing import Dict, Any
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

base_url = 'http://nfce.sefaz.pe.gov.br/nfce-web/consultarNFCe'
nf_code = '26220709515628000528650220001014011596828485|2|1|1|95FE53D7539468560309C8E1C560C9EF53329FE1'


class Collector:
    def __init__(self, code: str) -> None:
        self.code: str = code
        encoded_code: str = quote_plus(code)
        self.url: str = f'{base_url}?p={encoded_code}'

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


if __name__ == '__main__':
    collector = Collector(nf_code)
    response = collector.collect()
    print(response)
