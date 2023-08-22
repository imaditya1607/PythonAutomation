import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj = Service("c://drivers//msedgedriver.exe")
driver = webdriver.Edge(service=ser_obj)
myWait = WebDriverWait(driver, 10)

driver.get("http://www.opencart.com")
driver.find_element(By.XPATH, "//a[@class='btn btn-black navbar-btn']").click()

myWait.until(EC.title_contains("OpenCart - Account Register"))
register_page = driver.title
actual_page_title = "OpenCart - Account Register"
if register_page == actual_page_title:
    print("we have sucessfully launched registerpage")
else:
    print(f"{register_page} is not equal to {actual_page_title}")
    driver.close()
