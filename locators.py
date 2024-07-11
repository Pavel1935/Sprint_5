from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Войти в аккаунт (морда)
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input[@name='name']")  # Инпут имя
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input[@name='name']")  # Инпут email
    PASSWORD = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input[@name='Пароль']") # Инпут password
    REGISTER_BUTTON_MAIN = (By.XPATH, "//a[@href='/register']")  # Кнопка "Зарегистрироваться" (экран авторизации)
    AUTH_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button')]")  # Кнопка "Войти" (авторизация)
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"
    AUTH_TEXT = (By.XPATH, "//h2[contains(text(), 'Вход')]")  # Текст "Вход" (авторизация)
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение "Некорректный пароль"
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка "Войти" (регистрация)
    LOGIN_RECOVERY_BUTTON = (By.XPATH, "//a[contains(@class,'Auth_link__1fOlj')]")  # Кнопка "Войти" (восстановление пароля)
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")   # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    RECOVERY_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Кнопка "Восстановить пароль"
    REGISTER_BUTTON_1 = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться" (экран регистрации)
    COLLECT_BURGER_BUTTON = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")   # Кнопка "Соберите бургер" (экран регистрации)
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"
    SAUCE_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Кнопка "Соусы"
    SAUCE_SPACE_X = (By.XPATH, "//p[contains(text(),'Соус Spicy-X')]")  # Кнопка "Соус Spicy-X"
    BREAD_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")  # Кнопка "Булки"
    FLUR_BULKA = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")  # Кнопка "Флюр булка"
    INGREDIENTS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Кнопка "Начинки"
    BEEF_METEOR_INGREDIENTS = (By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]") # Кнопка "Говяжий метеорит"