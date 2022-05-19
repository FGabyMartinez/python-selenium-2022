import imp
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Inicializar Drivers
chrome_driver_path = "C:\Selenium\python-selenium-2022\drivers\chromedriver.exe"
gecko_driver_path = "C:\Selenium\python-selenium-2022\drivers\geckodriver.exe"
url = "https://Laboratorios.qaminds.com"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

#Abrir Pagina
driver.get(url)

#Buscar input usuario
time.sleep(5) #No es lo ideal para resolver el problema de carga
driver.find_element( ) 



#cerrar el navegador
time.sleep(3)
driver.quit()