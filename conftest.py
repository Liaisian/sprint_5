import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')

    URL = 'https://stellarburgers.nomoreparties.site'

    driver.get(URL)

    yield driver
    driver.quit()