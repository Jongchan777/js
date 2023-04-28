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

# print(driver.current_url)


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


# ['쇼핑'] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, '.css-ie1qvg')[2].click()
driver.implicitly_wait(10)
time.sleep(2)


rand_product = [0, 1, 2, 3]
rand_int = random.randint(0, 3)

# 랜덤 상품 가격 뽑기
selected_item = driver.find_elements(By.CSS_SELECTOR, ".css-17gm4gr")[rand_product[rand_int]]
selected_item_price = re.findall('\d+', selected_item.text)
#selected_item_price_value = int(''.join(selected_item_price))
selected_item_price_value = (''.join(selected_item_price))

if '5' in selected_item_price_value:
    selected_item_price_value = 5160
else:
    selected_item_price_value = 10310

print(selected_item_price_value)
"""
if selected_item_price_value:
    selected_item_price_value = 5160
    print(selected_item_price_value)
else:
    selected_item_price_value = 10310
    print(selected_item_price_value)
"""


selected_item.click()
driver.implicitly_wait(10)
time.sleep(2)

"""

# ['구매하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, ".css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)

# 토스트 팝업 ['구매하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, ".css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)


# ['사용하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, ".css-1faxemt").click()
driver.implicitly_wait(10)
time.sleep(2)

# ['모두 사용하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, ".css-vmk80s").click()
driver.implicitly_wait(10)
time.sleep(2)

# ['사용'] 버튼
driver.find_element(By.CSS_SELECTOR, "button[type=button].css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)

# ['결제하기'] 버튼을 선택
driver.find_element(By.CSS_SELECTOR, "button[type=submit].css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(6)

# 주문완료 페이지로 이동 후, ['쇼핑 계속하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, "button[type=button].css-3hyl58").click()
driver.implicitly_wait(10)
time.sleep(2)
"""
"""
# ['마이'] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, '.css-ie1qvg')[4].click()
driver.implicitly_wait(10)
time.sleep(2)

# ['주문/배송 조회] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, '.css-1wu441d')[4].click()
driver.implicitly_wait(10)
time.sleep(2)

# ['사용하기'] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, 'button[type=button].css-158aci8')[0].click()
driver.implicitly_wait(10)
time.sleep(2)

# ['결제정보'] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, 'div.css-17ogpgl')[2].click()
driver.implicitly_wait(10)
time.sleep(2)

# ['주문취소'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, '.css-7rqbez').click()
driver.implicitly_wait(10)
time.sleep(2)

# ['주문취소'] 버튼을 선택
driver.find_element(By.CSS_SELECTOR, "button[type=button].css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)

# input box 선택 및 내용 입력
ib=driver.find_element(By.CSS_SELECTOR, "textarea.css-bn1435")
driver.implicitly_wait(10)
time.sleep(2)
ib.click()
time.sleep(1)
rand_int2 = random.randint(0, 9)
test = ["JCtest1", "JCtest2", "JCtest3", "JCtest4", "JCtest5", "JCtest6", "JCtest7", "JCtest8", "JCtest9", "JCtest10"]
ib.send_keys(f"{test[rand_int2]}")
time.sleep(1)

# ['주문취소 요청'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, "button[type=button].css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)

# ['쇼핑 계속하기'] 버튼 선택
driver.find_element(By.CSS_SELECTOR, "button[type=button].css-3hyl58").click()
driver.implicitly_wait(10)
time.sleep(2)

# ['마이'] 버튼 선택
driver.find_elements(By.CSS_SELECTOR, '.css-ie1qvg')[4].click()
driver.implicitly_wait(10)
time.sleep(2)
"""

driver.quit()

# 속성을 추가하여 엘리먼트 뽑아내기
# driver.find_element(By.CSS_SELECTOR, "button([type=button][class=css-y4iqq8])").click()
#css-y4iqq8
#css-1oskcxy
"""
df = driver.fine_element(By.CSS_SELECTOR, ".css-1oskcxy")
print(df)
"""
"""
driver.find_element(By.CSS_SELECTOR, ".css-y4iqq8").click()
driver.implicitly_wait(10)
time.sleep(2)
"""


# driver.quit()

# 알림 버튼 선택하여 알림 페이지로
# driver.find_element(By.CSS_SELECTOR, '.material-icons-outlined').click()
# time.sleep(1)

# 뒤로가기 버튼 선택하여 홈으로
# driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
# time.sleep(1)

# 공지사항 버튼 선택하여 공지사항 페이지로
""" driver.find_elements(By.CSS_SELECTOR, '.mouse-cursor')[0].click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """

# 개인정보처리방침 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.mouse-cursor')[1].click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1)
"""

# 이용약관 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.mouse-cursor')[2].click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """

# FAQ 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.mouse-cursor')[3].click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """

# 1:1문의 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.mouse-cursor')[4].click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """

# 카드샵 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.css-1oskuwq')[1].click()
time.sleep(1) """
# 뒤로가기 버튼
""" driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """

# 쇼핑 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.css-1oskuwq')[2].click()
time.sleep(1) """
# 홈 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.css-1oskuwq')[0].click()
time.sleep(1) """

# 마이 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.css-1oskuwq')[3].click()
time.sleep(1) """
# 뒤로가기 버튼
""" driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(1) """


# + 버튼 선택
""" driver.find_element(By.CSS_SELECTOR, '.css-rwex6u').click()
time.sleep(2) """
# x 버튼 선택
""" driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div[3]/span/img').click()
time.sleep(2) """


# + 버튼 선택
""" driver.find_element(By.CSS_SELECTOR, '.css-rwex6u').click()
time.sleep(2) """
# 카드 생성하기 버튼
""" driver.find_elements(By.CSS_SELECTOR, '.img30')[0].click()
time.sleep(2) """
# 뒤로가기 버튼
""" driver.find_element(By.CSS_SELECTOR, '.material-icons').click()
time.sleep(2) """

# + 버튼 선택
""" driver.find_element(By.CSS_SELECTOR, '.css-rwex6u').click()
time.sleep(2) """

# 카드 구매하기에 대한 동작 없음
""" driver.find_elements(By.CSS_SELECTOR, '.img30')[1].click()
time.sleep(2) """
# 해당 버튼(카드 구매하기)에 대한 동작 현재 없음
# driver.find_element(By.CSS_SELECTOR, '.material-icons').click()

# x 버튼 선택
""" driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div[3]/span/img').click()
time.sleep(2) """

"""
driver.find_elements(By.CSS_SELECTOR, '.css-1oskuwq')[3].click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '.css-p8oyw9').click()
time.sleep(2)

"""
#driver.quit()