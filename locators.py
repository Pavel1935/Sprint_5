from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Войти в аккаунт (морда)
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input[@name='name']") # Инпут имя
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input[@name='name']") # Инпут email
    PASSWORD = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input[@name='Пароль']") # Инпут password
    REGISTER_BUTTON_MAIN = (By.XPATH, "//a[@href='/register']")
    # Кнопка "Зарегистрироваться" (экран авторизации)
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Кнопка "Войти" (авторизация)
    BUTTON_ORDER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]") # Кнопка "Оформить заказ"
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение "Некорректный пароль"
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]") # Кнопка "Войти" (регистрация)
    LOGIN_RECOVERY_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]")  # Кнопка "Войти" (восстановление пароля)
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]") # Кнопка "Личный кабинет"
    RECOVERY_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[2]/a[1]") # Кнопка "Восстановить пароль"
    REGISTER_BUTTON_1 = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]") # Кнопка "Зарегистрироваться" (экран регистрации)
    COLLECT_BERGER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/h1[1]") # Кнопка "Соберите бургер" (экран регистрации)
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"
    SAUCE_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]") # Кнопка "Соусы"
    SAUCE_SPACE_X = (By.XPATH, "//p[contains(text(),'Соус Spicy-X')]") # Кнопка "Соус Spicy-X"
    BREAD_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]") # Кнопка "Булки"
    FLUR_BULKA = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]/p[1]") # Кнопка "Флюр булка"
    INGREDIENTS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]") # Кнопка "Начинки"
    BEEF_METEOR_INGREDIENTS = (By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]") # Кнопка "Говяжий метеорит"