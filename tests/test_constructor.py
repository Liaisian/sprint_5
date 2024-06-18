from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestExitFromProfile:

     def test_positive_check_constructor_(self, driver):
        # заходим на страницу входа
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Ожидание и нажатие кнопки входа
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/div/button"))).click()

        # Ожидание и ввод email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//fieldset[1]/div/div/input"))).send_keys('liaisianzalotdinova9999@yandex.ru')

        # Ожидание и ввод пароля
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]"))).send_keys('T@ig@1507')

        # Ожидание и нажатие кнопки входа
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]'))).click()

        # Ожидание и нажатие на первый элемент конструктора
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//section[1]/div[1]'))).click()

        # Ожидание и нажатие на второй элемент конструктора
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//section[1]/div[1]/div[1]/span'))).click()

        # Ожидание и нажатие на третий элемент конструктора
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//section[1]/div[1]/div[3]/span'))).click()

        driver.quit()
