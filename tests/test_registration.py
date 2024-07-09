from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

faker = Faker()
class TestStellarBurger:

    def test_registration(self, driver):
        email = faker.email()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/register']"))).click()
        driver.find_element(*Locators.NAME).send_keys('Sprint')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_BUTTON_1)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "// h2[contains(text(), 'Вход')]"))).text == 'Вход'
    def test_registration_error(self, driver):
            driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
            driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
            driver.find_element(By.XPATH,
                                "//label[contains(text(),'Имя')]/following-sibling::input[@name='name']").send_keys('Sprint_5_error')
            driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
            driver.find_element(*Locators.PASSWORD).send_keys('12345')
            driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
            assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//p[@class='input__error text_type_main-default']"))).text == 'Некорректный пароль'