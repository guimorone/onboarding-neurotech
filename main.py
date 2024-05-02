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
        response = {}
        page = get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return response


if __name__ == '__main__':
    collector = Collector(nf_code)
    response = collector.collect()
    print(response)
