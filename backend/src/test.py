import unittest
from unittest.mock import patch
import requests
from requests.exceptions import ConnectTimeout
from bs4 import BeautifulSoup
from utils import encode_url
from constants import *


class TestCase(unittest.TestCase):
    def test_if_site_is_up(self) -> None:
        url = f'{BASE_URL}?p=' + encode_url(INITIAL_NF_CODE)
        with patch('requests.get') as mock_get:
            try:
                requests.get(url, timeout=TIMEOUT)
                mock_get.assert_called_once_with(url, timeout=TIMEOUT)
            except ConnectTimeout as error:
                self.fail('Site is down!\n' + str(error))

    def test_if_markup_changed(self) -> None:
        fail_msg = 'Markup has changed!'
        url = f'{BASE_URL}?p=' + encode_url(INITIAL_NF_CODE)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'xml')
        products = soup.find_all('prod')

        if not products or not len(products):
            self.fail(fail_msg)

        for product in products:
            code = product.find('cProd')
            name = product.find('xProd')
            qtd = product.find('qCom')
            unit_value = product.find('vUnCom')
            total_value = product.find('vProd')

            self.assertIsNotNone(code, fail_msg)
            self.assertIsNotNone(name, fail_msg)
            self.assertIsNotNone(qtd, fail_msg)
            self.assertIsNotNone(unit_value, fail_msg)
            self.assertIsNotNone(total_value, fail_msg)


if __name__ == '__main__':
    unittest.main()
