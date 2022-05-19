import email
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

my_account: WebElement = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
assert my_account.is_displayed(), "Menu is not available"
my_account.click()
time.sleep(2) 

login: WebElement = driver.find_element(By.LINK_TEXT,"Login")
assert login.is_displayed(), "Login is not available"
login.click()

time.sleep(2) 
email = driver.find_element(By.ID, "input-email")
assert email.is_displayed(), "Email is not availabe"
email.clear()
email.send_keys("Invalid")
time.sleep(2)

password = driver.find_element(By.ID, "input-password")
assert password.is_displayed, "pass is not availabe"
password.clear()
password.send_keys("Invalid")

login_btn:  WebElement = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
assert login_btn.is_displayed(), "Btn is not available"
login_btn.click()

error_msg = driver.find_element(By.XPATH, '//*[contains(@class,"fa fa-exclamation-circle")]')
assert error_msg.is_displayed(), "Error Message is not visible"

#cerrar el navegador
time.sleep(3)
driver.quit()