import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser():
    driver = Service("Skills/chromedriver/")
    pytest.driver = webdriver.Chrome(service=driver)

    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    pytest.driver.maximize_window()

    pytest.driver.implicitly_wait(10)

    yield pytest.driver

    pytest.driver.quit()