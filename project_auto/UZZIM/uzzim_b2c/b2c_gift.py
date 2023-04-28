from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains    # ActionChains 사용하기 위함
from random import randint # 랜덤 int값 사용하기 위함
# from requests import get
import pyautogui, time

driver = webdriver.Chrome("/Users/apple/jupyter_first_project/project_auto/UZZIM/uzzim_c2c/chromedriver")

# 접근할 URL
url="https://u-zzim-b2c-stage.travelflan.com/login"

# browser 오픈
driver.get(url)
driver.maximize_window()

# ActionChanins define
action = ActionChains(driver)

# 입력 대기
# id_pw_confirm = input("ID, PW를 입력 후, console에 엔터를 입력하세요")

# html 모든 값을 불러올때까지 최대 10초 대기
driver.implicitly_wait(10)
time.sleep(1)

# uzzim@bccard.com // pass
# testuser@freedgrouptech.com // pass

# 이메일 input box 찾기 및 선택 
driver.find_element(By.CSS_SELECTOR, 'input[type=text].css-x6yqmg').send_keys("uzzim@bccard.com", Keys.TAB)

time.sleep(1)

(
action.send_keys('pass')
.send_keys(Keys.TAB).send_keys(Keys.TAB)
.send_keys(Keys.ENTER)
.perform()
)

driver.implicitly_wait(10)
time.sleep(2)

# class 명이 css-1cp6lf7 인 값들을 찾아서, 세 번째 값을 선택
driver.find_elements(By.CSS_SELECTOR, 'div.css-1cjjkp9')[1].click()
driver.implicitly_wait(10)
time.sleep(2)

# class 명이 css-1iwfobh 인 값들을 찾아서, 첫 번째 값을 선택
driver.find_elements(By.CSS_SELECTOR, 'div.css-1iwfobh')[0].click()
driver.implicitly_wait(10)
time.sleep(2)

#['내 기프트 전체보기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, 'div.css-1ll7gpb').click()
driver.implicitly_wait(10)
time.sleep(1)

# 카드 카운팅 + 랜덤 선택 완료
first_card_count = driver.find_elements(By.CSS_SELECTOR, 'div.css-95uwek')
card_count = len(first_card_count) - 1
print(card_count)
rand_int = randint(6, card_count)
card_selector = driver.find_elements(By.CSS_SELECTOR, 'div.css-95uwek')[rand_int]
card_selector.click()
driver.implicitly_wait(10)
time.sleep(2)



"""
# 총 n개 + 6 - 1 = val
first_card.click()
driver.implicitly_wait(10)
time.sleep(3)
"""



"""
for i in range(3):
    card_choice = randint(0,4)
    driver.implicitly_wait(10)

    driver.find_elements(By.CSS_SELECTOR, '.css-v5fqpx')[card_choice].click()

    time.sleep(1)

    jc_number = randint(0,100)

    (
    action.send_keys(Keys.TAB)
    .send_keys(Keys.ENTER)
    .send_keys(f"김종찬{jc_number}")
    .send_keys(Keys.TAB).send_keys('01055066609')
    .perform()
    )

    driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()

    driver.find_element(By.CSS_SELECTOR, '.css-4ywbu1').click()

    jc_price = randint(1000, 200000)

    (
    action.send_keys(f"김종찬{jc_number}")
    .send_keys(Keys.TAB)
    .send_keys(Keys.TAB)
    .send_keys(f"김종찬{jc_number}")
    .send_keys(Keys.TAB)
    .send_keys(f"{jc_price}")
    .perform()
    )

    driver.find_element(By.CSS_SELECTOR, '.css-1y8cl30').click()

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()
    print(i)
    time.sleep(5)
"""

driver.quit()


"""
card_choice = randint(0,4)
driver.implicitly_wait(10)

driver.find_elements(By.CSS_SELECTOR, '.css-v5fqpx')[card_choice].click()

time.sleep(1)

jc_number = randint(0,100)

(
action.send_keys(Keys.TAB)
.send_keys(Keys.ENTER)
.send_keys(f"김종찬{jc_number}")
.send_keys(Keys.TAB).send_keys('01055066609')
.perform()
)

driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()

driver.find_element(By.CSS_SELECTOR, '.css-4ywbu1').click()

jc_price = randint(1000, 200000)

(
action.send_keys(f"김종찬{jc_number}")
.send_keys(Keys.TAB)
.send_keys(Keys.TAB)
.send_keys(f"김종찬{jc_number}")
.send_keys(Keys.TAB)
.send_keys(f"{jc_price}")
.perform()
)

driver.find_element(By.CSS_SELECTOR, '.css-1y8cl30').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.css-zx15nb').click()
"""

# .random() 해당 내장함수로 구현해볼 것


