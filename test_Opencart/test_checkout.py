from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage
from lib.pom.qaminds.checkout_page import CheckoutPage


class TestCheckoutPage:
    driver: WebDriver = None
    prod_page: ProductPage = None
    checkout_page: CheckoutPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.prod_page = ProductPage(self.driver)
        self.prod_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&path=57&product_id=49")
        self.prod_page.add_to_cart()
        self.prod_page.is_login_warn_displayed()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.goto("https://laboratorio.qaminds.com/index.php?route=checkout/checkout")


    def test_checkout_invalid_customer(self):
        invalid_email = "qatest22@gmail.com"
        password = "7913546"
        expected_error_msg = "Warning: No match for E-Mail Address and/or Password."
        assert expected_error_msg == self.checkout_page.login_with_invalid_credentials(invalid_email, password)


    def teardown_method(self):
        if self.driver:
            self.driver.quit()