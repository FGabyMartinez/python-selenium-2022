from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestSearchDisplay:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait utilizando la informacion de config.json
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_small())

        # Abrir la pagina web
        self.driver.get(config.get_url())

    def test(self):

        currency_locate = (By.XPATH, '//*[@id="form-currency"]//strong') #Verificar si funciona con el path del button //*[@id="form-currency"]//button
        currency: WebElement = self.wait.until(EC.element_to_be_clickable(currency_locate))
        assert currency.text == "$"

        search_input_locate = (By.NAME, "search")
        search_input: WebElement = self.wait.until(EC.element_to_be_clickable(search_input_locate))
        search_input.send_keys("Samsung")

        search_btn_locate = (By.XPATH, '//*[@id="search"]/span/button')
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_locate))
        search_btn.click()

        samsung_locate = (By.LINK_TEXT, "Samsung SyncMaster 941BW")
        samsung: WebElement = self.wait.until(EC.element_to_be_clickable(samsung_locate))
        samsung.click()

        price_locate = (By.XPATH, '  //*[@id="content"]/div/div[2]/ul[2]/li[1]/h2') # Para que sea mas seguro se puede usar proceding-sibling para llegar al h2 ejem: //*[@id='product']/preceding-sibling::ul//h2
        price_usd = WebElement = self.wait.until(EC.visibility_of_element_located(price_locate))
        price_usd = price.text

        dropdown_locate = (By.XPATH, '//*[@id="form-currency"]//ul/li[1]/button') # //*[@id="form-currency"]//button[@data-toggle="dropdown"]
        dropdown: WebElement = self.wait.until(EC.visibility_of_element_located(dropdown_locate))
        dropdown.click()

        btn_euro_locate = (By.NAME, "EUR")
        btn_euro: WebElement =self.wait.until(EC.element_to_be_clickable(btn_euro_locate))
        btn_euro.click()

        price: WebElement = self.wait.until(EC.visibility_of_element_located(price_locate))
        price_euro = price.text


        # imprimir precio en euros y usd
        print("")
        print(price_usd)
        print(price_euro)

        

    def teardown_method(self):
        if self.driver:
            self.driver.quit()