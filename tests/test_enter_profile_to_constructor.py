from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestEnterToConstructor:
    # переход из личного кабинета в конструктор
    def test_positive_enter_from_personal_profile_to_constructor(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, "//section[2]/div/button").click()

        # Явное ожидание появления поля ввода email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//fieldset[1]/div/div/input")))

        # Вводим имя и пароль
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys('liaisianzalotdinova9999@yandex.ru')

        # Вводим пароль
        driver.find_element(By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]").send_keys('T@ig@1507')

        # нажимаем на вход
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]').click()

        # Явное ожидание загрузки страницы входа в аккаунт
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, "//html/body/div/div/header/nav/a/p").click()

        # Явное ожидание появления кнопки конструктор
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div/header/nav/ul/li[1]/a/p")))

        # нажимаем на кнопку конструктор
        driver.find_element(By.XPATH, "//html/body/div/div/header/nav/ul/li[1]/a/p").click()

        # нажимаем на кнопку на кнопку личный кабинет
        driver.find_element(By.XPATH, "//html/body/div/div/header/nav/a/p").click()

        # нажимаем на логотип
        driver.find_element(By.XPATH, "//html/body/div/div/header/nav/div").click()

        # Получаем текущий URL
        current_url = driver.current_url

        # Ожидаемый URL страницы входа
        expected_url = "https://stellarburgers.nomoreparties.site/"

        # Проверяем, что текущий URL равен ожидаемому URL страницы входа
        assert current_url == expected_url, "Тест не прошел успешно"

        driver.quit()