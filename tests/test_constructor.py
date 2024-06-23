import time

from selenium.webdriver.common.by import By
from conftest import driver
from locators import Constructor_form_locators


class TestConstructorTransitions:
    def test_constructor_transitions_to_section(self, driver):
        # Нажать на вкладку "Булки"
        driver.find_element(*Constructor_form_locators.BREAD_TAB).click()
        #Проверка перехода в раздел "Булки"
        assert driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab_type_current")]').text == 'Булки'

        # Нажать на вкладку "Соусы"
        driver.find_element(*Constructor_form_locators.SAUCE_TAB).click()

        # Проверка перехода к разделу «Соусы»
        assert driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab_type_current")]').text == 'Соусы'

        # Нажать на вкладку "Начинки"
        driver.find_element(*Constructor_form_locators.FILLING_TAB).click()

        # Проверка перехода к разделу «Начинки»
        assert driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab_type_current")]').text == 'Начинки'

