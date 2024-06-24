from selenium.webdriver.common.by import By
from URL import URL_LOGIN, URL_ACCOUNT, URL_FORGOT_PASSWORD, URL_REGISTER
from conftest import driver
from locators import Main_page_locators, Login_form_locators, Header_locators
class TestEnterUser:
# тест входа на страницу войти на сайт
    def test_enter_user1(self, driver):
        # вход по кнопке «Войти в аккаунт»
        driver.find_element(*Main_page_locators.SIGN_IN_BUTTON).click()
        # Проверь, что открылась страница авторизации
        assert driver.current_url == URL_LOGIN

# тест входа в личный кабинет на сайте
    def test_enter_user2(self, driver):
         # вход по кнопке «Войти в аккаунт»
        driver.find_element(*Main_page_locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Login_form_locators.EMAIL_FIELD).send_keys('liaisianzalotdinova9999@yandex.ru')
        # вводим пароль
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys('T@ig@1507')
        # нажимаем на вход
        driver.find_element(*Login_form_locators.SIGN_IN_BUTTON).click()
        # Вход по кнопке «Личный кабинет»
        driver.find_element(Header_locators.PERSONAL_ACCOUNT_LINK).click()
        # Проверь, что открылась страница личного кабинета
        assert driver.current_url == URL_ACCOUNT

# тест входа на страницу авторизации из страницы регистрации
    def test_enter_user3(self, driver):
        driver.get(URL_REGISTER)
        # вход по кнопке "Войти» в форме регистрации
        driver.find_element(By.XPATH, "//html/body/div/div/main/div/div/p/a").click()
        # Проверь, что открылась страница авторизации
        assert driver.current_url == URL_LOGIN

# тест попасть на страницу входа через восстановление пароля
    def test_enter_user4(self, driver):
        driver.get(URL_FORGOT_PASSWORD)
        # вход через кнопку "Войти" в форме восстановления пароля
        driver.find_element(By.XPATH, "//html/body/div/div/main/div/div/p/a").click()
        # Проверь, что открылась страница восстановления пароля
        assert driver.current_url == URL_LOGIN





