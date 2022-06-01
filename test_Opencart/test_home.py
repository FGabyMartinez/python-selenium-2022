from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage

class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test(self):
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('Samsung')

    def test_menu(self):
        # 1. Dar click all menu 
        """home_page = HomePage(self.driver)
        home_page.select_menu("tablets")
        home_page.select_menu("software")"""
        for menu in ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]:
            self.select_menu(menu)

    def test_sub_menu(self): 
        # 1. Dar click al menu mp3 player -> all mp3
        # 2. Seleccionar ipod nano
        home_page = HomePage(self.driver)
        home_page.select_sub_menu("MP3 Players", "Show All MP3 Players")
        home_page.select_sub_menu('iPod Nano')  

    def test_currency(self): 
        # 1. Verificar currency, debe ser igual a $
        # 2. cambiar currency a euros
        home_page = HomePage(self.driver)
        assert "$" == home_page.get_currency()
        home_page.set_currency("EUR")
        assert "€" == home_page.get_currency()
        home_page.set_currency("Sterling")
        assert "£" == home_page.get_currency()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()