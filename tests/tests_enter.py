from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestEnterUser:
# тест входа на страницу войти на сайт
    def test_enter_user1(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        # вход по кнопке «Войти в аккаунт»
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()

        # Проверь, что открылась страница авторизации
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

# тест входа в личный кабинет на сайте
    def test_enter_user2(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        # вход по кнопке «Войти в аккаунт»
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()

        driver.find_element(By.XPATH,"//fieldset[1]/div/div/input").send_keys('liaisianzalotdinova9999@yandex.ru')

        # вводим пароль
        driver.find_element(By.XPATH,"//fieldset[2]/div[1]/div[1]/input[1]").send_keys('T@ig@1507')

        # нажимаем на вход
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]').click()

        # Вход по кнопке «Личный кабинет»
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/header[1]/nav[1]/a[1]").click()

        # Проверь, что открылась страница личного кабинета
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'


# тест входа на страницу авторизации из страницы регистрации

    def test_enter_user3(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")

        # вход по кнопке "Войти» в форме регистрации
        driver.find_element(By.XPATH, "//html/body/div/div/main/div/div/p/a").click()

        # Проверь, что открылась страница авторизации
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


# тест попасть на страницу входа через восстановить пароль
    def test_enter_user4(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # вход через кнопку "Войти" в форме восстановления пароля
        driver.find_element(By.XPATH, "//html/body/div/div/main/div/div/p/a").click()

        # Проверь, что открылась страница восстановления пароля
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()



