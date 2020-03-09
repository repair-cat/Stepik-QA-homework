import time
import math
import pytest
from selenium import webdriver


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_find_correct_answer(browser, link):
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))                             # ожидание перед каждым поиском элемента
    browser.get(link)
    input_ans = browser.find_element_by_tag_name("textarea")        # найти поле для ввода  
    input_ans.send_keys(str(answer))                                # ввести значение 
    button = browser.find_element_by_css_selector("button.submit-submission")     # найти кнопку Отправить
    button.click()                                                  # нажать кнопку
    correct_mes = browser.find_element_by_tag_name("pre")           # найти элемент сообщения после ответа
    assert "Correct!" in correct_mes.text