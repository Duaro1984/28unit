from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_phone, valid_password


# Тест сценария авторизации по номеру телефона
def test_auth_by_phone(driver):
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//section[@id="page-right"]/div/div/h1'), 'Авторизация')
    )
    # Вводим номер телефона
    phone_input = driver.find_element(By.ID, 'username')
    phone_input.send_keys(valid_phone)

    # Вводим пароль
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(valid_password)

    login_button = driver.find_element(By.ID, 'kc-login')
    login_button.click()

    # Ожидаем успешной авторизации или отображения сообщения об ошибке
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Константинов')
        )
    except:
        error_message = driver.find_element(By.ID, 'eform-error-message').text
        assert "Неверный логин или пароль" in error_message

