from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestEnterUser:

    # Тест вход в личный кабинет из страницы в личный кабинет personal profile"
    def test_positive_enter_in_personal_profile(self, driver):
        # заходим на страницу входа
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//section[2]/div/button").click()

        # Явное ожидание появления поля ввода email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//fieldset[1]/div/div/input")))

        # Вводим имя
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys('liaisianzalotdinova9999@yandex.ru')

        # Явное ожидание появления поля ввода пароля
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]")))

        # Вводим пароль
        driver.find_element(By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]").send_keys('T@ig@1507')

        # Явное ожидание появления кнопки входа
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]')))

        # нажимаем на вход
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]').click()

        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, "//html/body/div/div/header/nav/a/p").click()
        time.sleep(5)
        # Получаем текущий URL
        current_url = driver.current_url

        # Ожидаемый URL страницы входа в аккаунт
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"

        # Проверяем, что текущий URL содержит ожидаемый URL страницы входа в аккаунт
        assert expected_url in current_url, "Тест не прошел успешно"

        driver.quit()
