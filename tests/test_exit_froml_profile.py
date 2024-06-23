
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import Main_page_locators, Login_form_locators, Header_locators, Personal_account_locators


class TestExitFromProfile:

# выход из личного кабинета
    def test_positive_exit_from_personal_profile(self, driver):

        # Авторизация
        # Ожидание и нажатие кнопки входа в аккаунт из главной страницы
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Main_page_locators.SIGN_IN_BUTTON)).click()

        # Ожидание и ввод email на странице авторизации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.EMAIL_FIELD).send_keys('liaisianzalotdinova9999@yandex.ru')

        # Ожидание и ввод пароля на странице авторизации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(*Login_form_locators.PASSWORD_FIELD).send_keys('T@ig@1507')

        # Ожидание и нажатие на кнопку входа на странице авторизации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Login_form_locators.SIGN_IN_BUTTON).click()

        # Перезагрузка на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидание и нажатие кнопки личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Header_locators.PERSONAL_ACCOUNT_LINK).click()

        # Ожидание и нажатие кнопки выхода из личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Personal_account_locators.EXIT_BUTTON)).click()

        # Проверка текущего URL
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        current_url = driver.current_url

        # Ожидаемый URL страницы входа
        expected_url = "https://stellarburgers.nomoreparties.site/login"

        # Проверяем, что текущий URL равен ожидаемому URL страницы входа
        assert current_url == expected_url

