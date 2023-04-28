from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains    # ActionChains 사용하기 위함
from random import randint # 랜덤 int값 사용하기 위함


# from requests import get
import pyautogui
import time 
import pyperclip
import keyboard
import random
import re

# 아래 코드로 모바일 뷰로 실행 가능
# mobile_emulation = { "deviceName": "iPhone X" }
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Chrome("/Users/apple/Desktop/Python/chromedriver", options=chrome_options)

def c2c_login():
    driver = webdriver.Chrome("/Users/apple/jupyter_first_project/project_auto/UZZIM/uzzim_c2c/chromedriver")
    # 접근할 URL
    url="https://u-zzim-stage.travelflan.com/"

    # browser 오픈
    driver.get(url)

    # browser 최대화
    driver.maximize_window()
    action = ActionChains(driver)
    driver.implicitly_wait(10)
    time.sleep(2)

    # ['마이'] 버튼 선택
    driver.find_elements(By.CSS_SELECTOR, '.css-eb0qtc')[4].click()
    driver.implicitly_wait(10)
    time.sleep(2)

    # ['네이버 로그인'] 버튼 선택
    driver.find_element(By.CSS_SELECTOR, '.css-i5vm95').click()
    driver.implicitly_wait(10)
    time.sleep(2)

    """
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
    """

    # ID, PW 입력할 동안 대기
    name = pyautogui.confirm('Shall I proceed?')
    print(name)

    # confirm이 입력될 시, 로그인 진행
    log_ent = driver.find_element(By.ID, value="log.login")
    log_ent.click()
    driver.implicitly_wait(10)
    time.sleep(3)