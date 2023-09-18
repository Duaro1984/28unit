import datetime
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print(f"\nTest time: {end_time - start_time}")


@pytest.fixture(autouse=True)
def start_end():
    print("\n\n Test started!")
    yield
    print(" Test finished!")


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    yield driver

    driver.quit()
