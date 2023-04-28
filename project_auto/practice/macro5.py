from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import time

# Open Chrome browser
driver = webdriver.Chrome("/Users/apple/jupyter_first_project/chromedriver")

# Navigate to Naver login page
driver.get('https://nid.naver.com/nidlogin.login')


# pyperclip 기능 사용을 위한 입력
user_id = 'frhn00'
user_pw = 'my1199219!!@#'

log_id = driver.find_element(By.ID, value="id")
log_id.click()
time.sleep(2)
pyperclip.copy(user_id)
time.sleep(2)
log_id.send_keys(Keys.COMMAND, 'v')
time.sleep(2)


log_pid = driver.find_element(By.ID, value="pw")
log_pid.click()
time.sleep(2)
pyperclip.copy(user_pw)
time.sleep(2)
log_pid.send_keys(Keys.COMMAND, 'v')
time.sleep(2)


log_ent = driver.find_element(By.ID, value="log.login")
log_ent.click()
driver.implicitly_wait(10)
time.sleep(3)

# Wait for login to complete and page to load
time.sleep(5)

# Close browser
driver.quit()