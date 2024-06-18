
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestRegistration:

    def test_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        # Найди поле "Имя" и заполни его
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys('Liaisian')

         # Найди поле "Email" и заполни его
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys('liaisianzalotdinova9999@yandex.ru')

        # Найди поле "Пароль" и заполни его
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys('4550')

        # Нажми на кнопку "Зарегистрироваться" и кликни по ней
        driver.find_element (By.XPATH, "//*[contains(@class,'button_button_size_medium')]").click()

        # Проверяем, что в сообщении об ошибке текст 'Некорректный пароль'
        assert driver.find_element (By.XPATH,".//fieldset[3]/div/p").text == 'Некорректный пароль'

        driver.quit()

