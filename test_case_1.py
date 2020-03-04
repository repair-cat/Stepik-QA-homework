from selenium import webdriver
import time
import os

 
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


    # Ваш код, который заполняет обязательные поля
    
f_name = browser.find_element_by_name('firstname')
f_name.send_keys('Ivan')
l_name = browser.find_element_by_name('lastname')
l_name.send_keys('Vanko')
email = browser.find_element_by_name('email')
email.send_keys('Ivan@vanko')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_id('file') 
element.send_keys(file_path)

    # Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()