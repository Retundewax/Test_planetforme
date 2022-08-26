from appium import webdriver
from selenium.webdriver.common.by import By
import time

desired_capibilities = {
    'platformName': "Android",
    'platformVersion': "12",
    'deviceName': "Android Emulator",
    'app': "C:\\Users\\Dmitry\\Desktop\\Planet for me social network_v3.56.1883_apkpure.com.apk",
    'appActivity': 'com.planet.forme.ui.activities.main.MainActivity',
    'appPackage': 'com.planet.forme'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capibilities)
time.sleep(3)
driver.find_element(By.ID, 'com.planet.forme:id/logInTabButton').click()
time.sleep(1)
driver.find_element(By.ID, 'com.planet.forme:id/loginInput').click()
driver.find_element(By.ID, 'com.planet.forme:id/passwordInput').send_keys('Qpo40gpb11')
driver.find_element(By.ID, 'com.planet.forme:id/loginInput').send_keys('Retundewax')
driver.find_element(By.ID, 'com.planet.forme:id/signInButton').click()
driver.find_element(By.ID, 'com.planet.forme:id/navigationGlobalSearch').click()
driver.find_element(By.ID, 'com.planet.forme:id/searchEditText').send_keys('Москва')
try:
    ddd = driver.find_elements(By.ID, 'com.planet.forme:id/tvLogin')
except:
    ddd = []
    print('Ошибка')

def test_results():
    assert len(ddd) > 0






