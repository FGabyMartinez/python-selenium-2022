import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Inicializar Drivers
chrome_driver_path = "C:\Selenium\python-selenium-2022\drivers\chromedriver.exe"
gecko_driver_path = "C:\Selenium\python-selenium-2022\drivers\geckodriver.exe"
url = "https://laboratorio.qaminds.com"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
from selenium.webdriver.remote.webelement import WebElement

#Abrir Pagina
driver.get(url)
time.sleep(2) 

search_menu: WebElement = driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[4]/a")
assert search_menu.is_displayed(), "Menu tablet is not visible"
search_menu.click()
time.sleep(2) 

tablet_samsung = driver.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
assert tablet_samsung.is_displayed(), "Does not exists"
tablet_samsung.click()
time.sleep(2) 

search_price = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2') 
assert search_price.is_displayed(), "Search price is not visible"
assert search_price.text == "$241.99", "price is not 241.99"

add_to_cart = driver.find_element(By.ID, "button-cart")
assert add_to_cart.is_displayed(), "Button disable"
add_to_cart.click()


#cerrar el navegador
time.sleep(3)
driver.quit()