from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
wait = WebDriverWait(browser, 12)
wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button1 = wait.until(EC.element_to_be_clickable((By.ID, "book")))
button1.click()

browser.execute_script("window.scrollBy(0, 200);")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element_by_id('input_value').text
y = calc(x)
input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

# нажатие на кнопку
button = browser.find_element_by_id("solve")
button.click()

time.sleep(10)
browser.quit()
