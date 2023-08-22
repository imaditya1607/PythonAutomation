import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("c://drivers//msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
driver.implicitly_wait(2)
actual_title = driver.title
expected_title = "Dashboard / nopCommerce administration"
if actual_title == expected_title:
    print("successfully launched homepage")
else:
    print(f"actual = {actual_title} is not matching with expected = {expected_title}")

driver.close()
