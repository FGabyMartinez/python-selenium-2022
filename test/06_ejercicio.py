import time
from pytest import Item
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

chrome_driver_path = 'C:\Selenium\python-selenium-2022\drivers\chromedriver.exe'
#gecko_driver_path = 'C:\Selenium\python-selenium-2022\drivers\geckodriver.exe'
url = "https://demoqa.com/select-menu"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Web Page
driver.get(url)
time.sleep(2)

cars = driver.find_element(By.ID, "cars")
assert cars.is_displayed(), "Cars is no visible"
cars_dropdown = Select(cars)

cars_dropdown.select_by_visible_text("Volvo")
cars_dropdown.select_by_visible_text("Audi")
selected_options: list = [item.text for item in cars_dropdown.all_selected_options]
assert "Volvo" in selected_options, "Volvo not selected"
assert "Audi" in selected_options, "Audi not Selected"
time.sleep(2)

driver.quit()