import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains # Action Chain


# element_to_be_clickable() 웹 요소가 클릭 가능한 상태일 때까지 기다림.
# visibility_of_element_located() 웹 요소가 실제로 보일 때까지 기다림.
# text_to_be_present_in_element() 웹 요소 안에 텍스트가 로딩될 때까지 기다림.
# invisibility_of_element_located() 웹 요소가 안 보일 때까지 기다림.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://workey.codeit.kr/costagram/index')


wait = WebDriverWait(driver, 3)
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

pw_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

#df

driver.quit()