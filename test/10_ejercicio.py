from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'C:\Selenium\python-selenium-2022\drivers\chromedriver.exe'
#gecko_driver_path = 'C:\Selenium\python-selenium-2022\drivers\geckodriver.exe'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5)

driver.get(url)

locator_btn = (By.ID, "autoclosable-btn-success")
btn : WebElement = wait.until(EC.element_to_be_clickable(locator_btn))
btn.click()

text_one = (By.CLASS_NAME, "alert-autocloseable-success")

wait.until(EC.visibility_of_element_located(text_one))

assert wait.until(EC.invisibility_of_element_located(text_one))

driver.quit()
