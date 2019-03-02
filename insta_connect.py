import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


# options = Options()
# options.add_argument("--headless")
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
assert "Instagram" in driver.title
buttonelem = driver.find_element_by_tag_name("button")
# for s in buttonelems:
#   if "Facebook" in s.text:
buttonelem.click()
assert "Log into Facebook" in driver.title
nameelement = driver.find_element_by_id("email")
passelement = driver.find_element_by_id("pass")
nameelement.send_keys("07026424711")
# nameelement.clear()
passelement.send_keys("t19sx1t1")
# passelement.clear()
buttonelem = driver.find_element_by_tag_name("button")
buttonelem.click()

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

#driver.close()