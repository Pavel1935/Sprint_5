from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

faker = Faker()
class TestStellarBurger:

    def test_registration(self, driver):
        email = faker.email()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located
                                       (Locators.REGISTER_BUTTON_MAIN)).click()
        driver.find_element(*Locators.NAME).send_keys('Sprint')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                        (Locators.REGISTER_BUTTON_1)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                               (Locators.AUTH_TEXT)).text == 'Вход'

    def test_registration_error(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON_MAIN).click()
        driver.find_element(*Locators.NAME).send_keys('Sprint_15_error')
        driver.find_element(*Locators.EMAIL).send_keys('Sprint_5@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(1234)
        driver.find_element(*Locators.REGISTER_BUTTON_1).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.PASSWORD_ERROR)).text == 'Некорректный пароль'