import re
from typing import Any
from logging import getLogger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Crawler(object):

    def __init__(self, url) -> None:
        self.logger = getLogger(__name__)
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        import os
        #os.environ.setdefault('webdriver.chrome.driver','/home/yoav/.virtualenvs/botify/lib/chromedriver')
        #options = Options()
        # options.add_argument("start-maximized")
        # options.add_argument("disable-infobars")
        # options.add_argument("--ignore-certificate-errors")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--test-type")
        self.driver = Chrome()
        try:
            assert regex.match(url) is not None

            self.driver.get(url)
            self.driver.maximize_window()

        except Exception as e:
            self.logger.exception(e)
            self.driver.quit()

    def inject(self):
        self.driver.execute_script(
            "Array.prototype.slice.call(document.getElementsByTagName('*')).forEach(a=> {a.addEventListener('click', function(event){ if (a == document.activeElement){alert(a.tagName);}})})")

    def quit(self):
        self.driver.quit()