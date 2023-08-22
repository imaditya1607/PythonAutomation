from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("c://drivers//msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)

driver.get("https://jqueryui.com/")
date_picker_option = driver.find_element(By.XPATH, "//*[@id='sidebar']/aside[2]/ul/li[6]/a")
date_picker_option.click()

date_picker_title = driver.find_element(By.XPATH, "//h1[@class='entry-title']").text
if date_picker_title == "Datepicker":
    print("we are in date picker page")
else:
    print("we are unable to launch date picker page ")
    driver.close()

date_picker_frame = driver.find_element(By.XPATH, "//*[@class='demo-frame']")
driver.switch_to.frame(date_picker_frame)
date_input = driver.find_element(By.XPATH, "//input[@class='hasDatepicker']")
date_input.click()

exp_date = 16
exp_month = "july"
exp_year = "1999"

visible_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
visible_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

lessThen__button = driver.find_element(By.XPATH, "//*[@class='ui-icon ui-icon-circle-triangle-w']")
greaterThen_button = driver.find_element(By.XPATH, "//a[@class='ui-datepicker-next ui-corner-all']']")

while exp_year < visible_year:
    greaterThen_button.click()

while exp_year > visible_year:
    lessThen__button.click()
