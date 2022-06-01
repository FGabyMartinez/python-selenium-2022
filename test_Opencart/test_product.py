from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.product_page import ProductPage
from lib.pom.qaminds.home_page import HomePage

class TestSearch:
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def search(self):
        #busqueda
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('ipod')

        home_page = HomePage(self.driver)
        assert home_page.select_product("iPod Shuffle"), "Product should be visible"
        home_page._click()

class TestProductPage:
    driver: WebDriver = None
    product_page: ProductPage = None

    """def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&path=33&product_id=31")"""

    def test_get_product_information(self):
        description = """Born to be worn.
        Clip on the worlds most wearable music player and take up to 240 songs with you anywhere. Choose from five colors including four new hues to make your musical fashion statement.
        Random meets rhythm.
        With iTunes autofill, iPod shuffle can deliver a new musical experience every time you sync. For more randomness, you can shuffle songs during playback with the slide of a switch.
        Everything is easy.
        Charge and sync with the included USB dock. Operate the iPod shuffle controls with one hand. Enjoy up to 12 hours straight of skip-free music playback."""
        assert self.product_page.get_name() == "iPod Shuffle"
        assert self.product_page.get_description() == description
        assert self.product_page.get_price() == "$122.00"
        assert self.product_page.get_ex_tax() == "100.00"
        assert self.product_page.get_product_code() == "Product 7"
        assert self.product_page.get_availability() == "In Stock"
    
    def test_add_to_cart(self):
        self.product_page.add_to_cart()  

    def teardown_method(self):
        if self.driver:
            self.driver.quit()       