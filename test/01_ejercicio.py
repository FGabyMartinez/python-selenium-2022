
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from lib.factory.factory_driver import get_driver

get_driver("firefox")


#Inicializar Drivers
chrome_driver_path = "C:\Selenium\python-selenium-2022\drivers\chromedriver.exe"
gecko_driver_path = "C:\Selenium\python-selenium-2022\drivers\geckodriver.exe"
url = "https://laboratorio.qaminds.com"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

#Abrir Pagina
driver.get(url)


#Buscar input
search: WebElement = driver.find_element(By.NAME,"search") 
assert search.is_displayed(), "Search is not visible"
search.send_keys("iphone")

search_btn: WebElement = driver.find_element(By.XPATH, "//*[@id='search']//button")
assert search_btn.is_displayed(), "Search Button is not visible"
search_btn.click()



#cerrar el navegador
time.sleep(3)
driver.quit()