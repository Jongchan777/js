from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains    # ActionChains 사용하기 위함
from random import randint # 랜덤 int값 사용하기 위함
# from requests import get
import pyautogui, time



driver = webdriver.Chrome("/Users/apple/Desktop/Python/python_project/selenium/chromedriver")
# 접근할 URL
url="https://u-zzim-b2c-dev.travelflan.com/login"

# browser 오픈
driver.get(url)
driver.maximize_window()



# ActionChanins define
action = ActionChains(driver)

# 입력 대기
# id_pw_confirm = input("ID, PW를 입력 후, console에 엔터를 입력하세요")

# html 모든 값을 불러올때까지 최대 10초 대기
driver.implicitly_wait(10)


# uzzim@bccard.com // pass
# testuser@freedgrouptech.com // pass

# 이메일 input box 찾기 및 선택 
driver.find_element(By.XPATH, '//*[@id="__next"]/div/section/div/form/div/div[1]/div/div/input').send_keys("uzzim@bccard.com", Keys.TAB)

(
action.send_keys('pass')
.send_keys(Keys.TAB).send_keys(Keys.TAB)
.send_keys(Keys.ENTER)
.perform()
)

driver.implicitly_wait(10)

# class 명이 css-1cp6lf7 인 값들을 찾아서, 세 번째 값을 선택
driver.find_elements(By.CSS_SELECTOR, '.css-1cjjkp9')[2].click()
time.sleep(1)
# class 명이 css-1iwfobh 인 값들을 찾아서, 첫 번째 값을 선택
driver.find_elements(By.CSS_SELECTOR, '.css-1iwfobh')[0].click()
driver.implicitly_wait(10)
time.sleep(3)












# 몇개 카드 생성할래?
for i in range(5):
    # 페인트버튼 = Point(x=1644, y=241)
    pyautogui.click(x=1518, y=247)

    # 스크롤 아래로 100만큼
    pyautogui.scroll(-100)
    time.sleep(1)

    #9개 색 중, 선택
    rand_int = randint(0,8)
    rand_color =['gray.png', 'black.png', 'blue.png', 'green.png', 'yellow.png', 'orange.png', 'pink1.png', 'pink2.png', 'purple.png']
    rand_sellect_color= pyautogui.locateCenterOnScreen(rand_color[rand_int]) #, confidence=0.9, grayscale=True
    pyautogui.click(rand_sellect_color.x/2, rand_sellect_color.y/2)
    time.sleep(1)

    # 스크롤 위로 100만큼
    pyautogui.scroll(100)
    #pyautogui.moveTo(rand_sellect_color, rand_sellect_color)
    time.sleep(1)

    # 완료 버튼
    pyautogui.click(x=1742, y=241)
    time.sleep(1)

    # 드로윙 버튼 선택
    drawing_imoge=pyautogui.locateCenterOnScreen('drawing.png')
    pyautogui.click(drawing_imoge.x/2, drawing_imoge.y/2)
    time.sleep(1)

    #드로윙 시작지점 설정
    pyautogui.click(1060, 525)

    # 랜덤 드로윙
    for i in range(20):
        x = randint(940,1190)
        y = randint(330,740)
        pyautogui.dragTo(x, y, button='left')
    time.sleep(1)

    # 완료 버튼
    pyautogui.click(x=1742, y=241)

    # 설정 버튼 선택
    time.sleep(1)
    pyautogui.click(x=377, y=240)

    # 발행하기 버튼 선택
    time.sleep(1)
    pyautogui.click(x=394, y=434)

    # 스크롤 아래로 100만큼
    time.sleep(1)
    pyautogui.scroll(-100)

    #카드 발행하기 버튼 선택
    time.sleep(1)
    pyautogui.click(x=1075, y=600)

    time.sleep(1)
    pyautogui.click(x=955, y=515)

    time.sleep(1)
    driver.get(driver.current_url)
    time.sleep(2)
    pyautogui.scroll(100)
    # 카드 선물하러 가기 : 1175, 515 / 확인 : 955, 515