from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


URL = 'https://yandex.ru/'
driver = webdriver.Chrome(executable_path='C:\\proekti_piton\\Tests_1\\venv\\chromedriver.exe')
driver.get(url=URL)
driver.maximize_window()
search_field = driver.find_element('xpath', '//div[@class="search2__input"]//input[@class="input__control input__input mini-suggest__input"]')
search_field.send_keys('Planet for me')
yandex_naiti = driver.find_element('xpath', '//button[@class="button mini-suggest__button button_theme_search button_size_search i-bem button_js_inited"]')
yandex_naiti.click()
nahodim_sait = driver.find_elements('xpath', '//div[@class="VanillaReact OrganicTitle OrganicTitle_multiline Typo Typo_text_l Typo_line_m organic__title-wrapper"]//a')

try:
    for i in nahodim_sait:
        if i.get_attribute('href') == 'https://planetfor.me/':
            i.click()
            break
except:
    print('нет результатов https://planetfor.me/!!!')


driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

planetforme_naiti = driver.find_element('xpath', '//input[@class="ml-8"]')
planetforme_naiti.click()
planetforme_naiti.send_keys('qa')
planetforme_naiti.send_keys(Keys.RETURN)
time.sleep(3)
def test_poslednii():
    assert driver.find_element('xpath', '//div[@class="items-container"]')

