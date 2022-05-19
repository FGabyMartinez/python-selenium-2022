from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'C:\Selenium\python-selenium-2022\drivers\chromedriver.exe'
#gecko_driver_path = 'C:\Selenium\python-selenium-2022\drivers\geckodriver.exe'
url = 'https://demo.seleniumeasy.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

modal = (By.ID, "at-cv-lightbox-win")
close_modal = wait.until(EC.visibility_of_element_located(modal))

btn_modal: WebElement = driver.find_element(By.LINK_TEXT, 'No, thanks!')
assert btn_modal.is_displayed(), "Btn is not enable"
btn_modal.click()

driver.quit()