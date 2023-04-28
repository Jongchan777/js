
# Import the required Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import datetime

# Set the path to the web driver
driver_path = "/Users/apple/jupyter_first_project/chromedriver"

# Create a new instance of the Chrome browser
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to the Naver website
driver.get('https://www.naver.com')

# Find the search input field and enter a search term
search_field = driver.find_element(By.NAME, 'query')
search_field.send_keys('example search term')
search_field.send_keys(Keys.RETURN)

# Verify that the search results page is displayed
assert 'example search term' in driver.title
"""
# Find the first search result and click on it
search_result = driver.find_element(By.CSS_SELECTOR, '.lnk_tit:nth-child(1)')
search_result.click()

# Verify that the expected page is displayed
assert 'Expected Page Title' in driver.title
"""
# Extract the test results to an Excel file
workbook = Workbook()
sheet = workbook.active
sheet['A1'] = 'Test Result'
sheet['B1'] = 'Timestamp'
sheet['A2'] = 'Pass'
sheet['B2'] = datetime.datetime.now()
sheet['B2'].number_format = 'yyyy년 mm월 dd일 hh시 mm분 ss초'

workbook.save('test_results.xlsx')

# Close the browser window
driver.close()
