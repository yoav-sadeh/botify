import os
import re
from typing import Any
from logging import getLogger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Crawler(object):

    def __init__(self, url = 'http://google.com') -> None:
        self.logger = getLogger(__name__)
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = Chrome(chrome_options=options)
        #self.driver = Chrome()
        try:
            self._assert_url(url)

            self.driver.get(url)
            self.driver.maximize_window()

        except Exception as e:
            self.logger.exception(e)
            self.driver.quit()

    def _assert_url(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        assert regex.match(url) is not None

    def inject(self):
        dirname = os.path.dirname(__file__)
        js = open(os.path.join(dirname, 'js/crawler.js'), 'r').read()
        self.driver.execute_script(js)

    def quit(self):
        self.driver.quit()