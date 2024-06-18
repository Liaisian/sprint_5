from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestExitFromProfile:

# выход из личного кабинета
    def test_positive_exit_from_personal_profile(self, driver):
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

        # Перезагрузка на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидание и нажатие кнопки личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div/header/nav/a/p"))).click()

        # Ожидание и нажатие кнопки выхода из личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div/main/div/nav/ul/li[3]/button"))).click()

        # Проверка текущего URL
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        current_url = driver.current_url

        # Ожидаемый URL страницы входа
        expected_url = "https://stellarburgers.nomoreparties.site/login"

        # Проверяем, что текущий URL равен ожидаемому URL страницы входа
        assert current_url == expected_url, "Тест не прошел успешно"

        driver.quit()