from itertools import product
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestAddDesktops:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait utilizando la informacion de config.json
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_small())

        # Abrir la pagina web
        self.driver.get(config.get_url())

    def test(self):
        desktops_menu_locator = (By.LINK_TEXT, 'Desktops')
        desktops_menu: WebElement = self.wait.until(EC.element_to_be_clickable(desktops_menu_locator))
        desktops_menu.click()

        mac_locator = (By.PARTIAL_LINK_TEXT, "Mac") #Se usa PARTIAL_LINK_TEXT y no LINK_TEXT porque tiene un numero y si cambia puede romper la busqueda
        mac: WebElement = self.wait.until(EC.element_to_be_clickable(mac_locator))
        mac.click()

        imac_locate = (By.LINK_TEXT, "iMac")
        imac: WebElement = self.wait.until(EC.element_to_be_clickable(imac_locate))
        imac.click()

        addtocard_locate =(By.ID, "button-cart")
        addtocard: WebElement = self.wait.until(EC.element_to_be_clickable(addtocard_locate))
        addtocard.click()

        msg_succes_locate = (By.CLASS_NAME, "alert-success")
        msg_succes ="Success: You have added"
        assert self.wait.until(EC.text_to_be_present_in_element(msg_succes_locate, msg_succes))
        """msg_succes:WebElement = self.wait.until(EC.visibility_of_element_located(msg_succes_locate))
        msg_succes = msg.text 
        Incorrecto
        """

        price_locate = (By.ID, "cart-total")
        price_total = " 1 item(s) - $122.00"
        assert self.wait.until(EC.text_to_be_present_in_element(price_locate, price_total))

        pass

    def teardown_method(self):
        if self.driver:
            self.driver.quit()