import unittest
from unittest.mock import patch
import requests
from requests.exceptions import ConnectTimeout
from utils import encode_url
from constants import *


class TestCase(unittest.TestCase):
    def test_if_site_is_up(self):
        url = encode_url(f'{BASE_URL}?p={INITIAL_NF_CODE}')
        with patch('requests.get') as mock_get:
            try:
                requests.get(url, timeout=10)
                mock_get.assert_called_once_with(url, timeout=10)
            except ConnectTimeout as error:
                self.fail('Site is down!\n' + str(error))


if __name__ == '__main__':
    unittest.main()
