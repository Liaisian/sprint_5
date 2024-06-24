
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import URL_LOGIN, URL_MAIN
from conftest import driver, login
from locators import Header_locators, Personal_account_locators

class TestExitFromProfile:
# выход из личного кабинета
    def test_positive_exit_from_personal_profile(self, driver, login):
        # Перезагрузка на главную страницу
        driver.get(URL_MAIN)
        # Ожидание и нажатие кнопки личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        # Ожидание и нажатие кнопки выхода из личного кабинета
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(*Personal_account_locators.EXIT_BUTTON)).click()
        # Проверка текущего URL
        WebDriverWait(driver, 10).until(EC.url_to_be(URL_LOGIN))
        current_url = driver.current_url
        # Ожидаемый URL страницы входа
        expected_url = URL_LOGIN
        # Проверяем, что текущий URL равен ожидаемому URL страницы входа, осуществлен переход на страницу авторизации
        assert current_url == expected_url

