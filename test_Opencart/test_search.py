from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestSearch:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def search(self):
        #busqueda de componenten samsung
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('Samsung')

        #busqueda de producto Canon
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('Canon')

        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('mac')

        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('ipod')

        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('palm')

        home_page = HomePage(self.driver)
        assert home_page.select_product("Palm Treo Pro"), "Product should be visible"
        home_page._click()

        """for search in ["Canon", "samsung", "iMac", "ipod", "palm"]:
            self.home_page.search(search)"""

    def teardown_method(self):
        if self.driver:
            self.driver.quit()   