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

# Open Web Page
driver.get(url)

# 
locator = (By.ID, 'downloadButton')
btn_download: WebElement = wait.until(EC.element_to_be_clickable(locator))
assert btn_download.is_displayed(), "Btn is not enable"
btn_download.click()

file = (By.XPATH, '//*[@id="dialog"]/div[1]')
download_File: WebElement = wait.until(EC.visibility_of_element_located(file))


btn_close = (By.CLASS_NAME, "ui-dialog-buttonset")
close_download: WebElement = wait.until(EC.element_to_be_clickable(btn_close))
close_download.click()

driver.quit()


