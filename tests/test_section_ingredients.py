from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

class TestStellarBurger:
    def test_section_ingredients(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located
                                       ((By.XPATH, "//span[contains(text(),'Начинки')]"))).click()
        assert WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located
                                              ((By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]"))).text == 'Говяжий метеорит (отбивная)'