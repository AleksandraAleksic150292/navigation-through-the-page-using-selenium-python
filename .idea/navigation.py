from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://career.luxoft.com/locations/serbia/")

time.sleep(3)

btnCookie = driver.find_element(By.LINK_TEXT,"ACCEPT")
btnCookie.send_keys(Keys.ENTER)

field = driver.find_element(By.NAME,"keyword")
searchJob = "QA Automation"
field.send_keys(searchJob)
field.send_keys(Keys.ENTER)
time.sleep(3)

positionField = driver.find_element(By.CLASS_NAME,"career-jobs__input")
positionField.send_keys("QA Automation")
time.sleep(3)

countriesField = driver.find_element(By.ID, "search_countries")
drp=Select(countriesField)
drp.select_by_visible_text("Serbia")
time.sleep(3)

citiesField = driver.find_element(By.ID,"search_cities")
drp2=Select(citiesField)
drp2.select_by_visible_text("Belgrade")
time.sleep(3)

specializationsField = driver.find_element(By.ID,"search_type")
drp3=Select(specializationsField)
drp3.select_by_visible_text("Python")
time.sleep(3)

btnSearch = driver.find_element(By.CSS_SELECTOR,".luxoft-career .career-jobs__btn")
btnSearch.send_keys(Keys.ENTER)
time.sleep(3)

menu = driver.find_element(By.CSS_SELECTOR,".nav__icon-mobile")
menu.click()
time.sleep(3)
jobOpportunities = driver.find_element(By.LINK_TEXT, "JOB OPPORTUNITIES")
jobOpportunities.send_keys(Keys.ENTER)