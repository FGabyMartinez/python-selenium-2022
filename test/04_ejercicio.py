from lib2to3.pgen2.driver import Driver
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

notebook_laptops = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
assert notebook_laptops.is_displayed(), "Laptops & Notebooks is not visible"
notebook_laptops.click()

time.sleep(2)
windows = driver.find_element(By.PARTIAL_LINK_TEXT, "Windows")
assert windows.is_displayed(), "Windows is not visible"
windows.click()

content = driver.find_element(By.XPATH, ("//*[@id='content']/p"))
assert content.is_displayed(), "El contenido no es visible"
assert content.text == "There are no products to list in this category.", "Windows is not empty"

time.sleep(2)
continue_btn = driver.find_element(By.LINK_TEXT, "Continue")
assert continue_btn.is_displayed(), "Continue is not visible"
continue_btn.click()

#cerrar el navegador
time.sleep(3)
driver.quit()


