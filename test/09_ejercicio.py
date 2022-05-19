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

# Verify progress label
progress_label_loc = (By.CLASS_NAME, "progress-label")  # XPATH: //*[@class='progress-label']
wait.until(EC.text_to_be_present_in_element(progress_label_loc, "Complete!"))

# Verify continue button
close_btn_local = (By.XPATH, "//button[text()='Close']")
close_btn: WebElement = wait.until(EC.element_to_be_clickable(close_btn_local))
close_btn.click()
