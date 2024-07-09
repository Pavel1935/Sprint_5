from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

class TestStellarBurger:
    def test_registration(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Соусы')]"))).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Булки')]"))).click()
        assert WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]/p[1]"))).text == 'Флюоресцентная булка R2-D3'
        # BREAD_R2_D3 =