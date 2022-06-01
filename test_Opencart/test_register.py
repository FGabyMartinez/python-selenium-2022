from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.register_page import RegisterPage


class TestRegister:
    driver: WebDriver = None
    register_page: RegisterPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.register_page = RegisterPage(self.driver)
        self.register_page.goto(
            "https://laboratorio.qaminds.com/index.php?route=account/register")

    def test_register_submit_incomplete_form(self):
        self.register_page.submit_an_incomplete_form()
        first_name = "test"
        last_name = "valid"
        phone = "151166001100"
        expected_error_msg_password_name = "Password must be between 4 and 20 characters!"
        assert expected_error_msg_password_name == self.register_page.complete_form_valid_values(first_name, last_name, phone)
        assert expected_error_msg_password_name == self.register_page.get_password_error()
    
    def test_register_user_with_invalid_info(self):
        first_name = "testetqanoesvalidoporquetienemasde32caracteres"
        last_name = "noesvalidoporquetienemasde32caracteres"
        phone = "151166001100"
        password = "98"
        confirm_password = "98"
        expected_error_msg_first_name = "First Name must be between 1 and 32 characters!"
        expected_error_msg_last_name = "Last Name must be between 1 and 32 characters!"
        expected_error_msg_password_name = "Password must be between 4 and 20 characters!"
        assert expected_error_msg_password_name == self.register_page.complete_form_invalid_values(first_name, last_name, password, confirm_password)
        assert expected_error_msg_password_name == self.register_page.get_password_error()
    
    def test_register_user_with_valid_info(self):
        first_name = "test"
        last_name = "valid"
        phone = "151166001100"
        password = "987654"
        confirm_password = "987654"
        expected_successful_msg = "Your Account Has Been Created!"
        assert expected_successful_msg == self.register_page.complete_form_valid_values(first_name, last_name, phone, password,
        confirm_password)


    def teardown_method(self):
        if self.driver:
            self.driver.quit()