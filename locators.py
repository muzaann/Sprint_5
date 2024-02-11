from selenium.webdriver.common.by import By
class TestLocators:
    PERSONAL_AREA = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/account']" #Личный кабинет
    REGISTRATION = By.XPATH, ".//a[contains(@class, 'Auth_link') and @href= '/register']" #Зарегестрироваться
    REGISTRATION_NAME = By.XPATH, ".//label[text()= 'Имя']/parent::div/input" #Имя при регистрации
    REGISTRATION_EMAIL = By.XPATH, ".//label[text()= 'Email']/parent::div/input"  #Email при регистрации
    REGISTRATION_PASSWORD = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"  #Пароль при регистрации
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()= 'Зарегистрироваться']" #Кнопка зарегистрироваться
    REGISTRATION_BLOK = By.XPATH, ".//form[contains(@class, 'Auth_form')]" #блок регистрации
    UNVALID_PASSWORD = By.XPATH, ".//p[@class= 'input__error text_type_main-default']" #сообщение о некорректном пароле
    AUTH_BUTTON_MAIN = By.XPATH,".//button[text()= 'Войти в аккаунт']" #Кнопка Войти на главной странице
    ACCOUNT = By.XPATH, ".//a[text()='Профиль']" #Кнопка профиль в личном кабинете
    ACCOUNT_EXIT = By.XPATH, "//button[text()= 'Выход']" #Кнопка выхода из аккаунта
    CONSTRUCTOR = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/']" #Конструктор бургеров
    ASSEMBLE_A_BURGER = By.XPATH, ".//h1[text()='Соберите бургер']" #Блок Соберите бургер
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]" #Логотип
    INPUT_EMAIL = By.XPATH, ".//label[text()= 'Email']/parent::div/input" #Email при авторизации
    INPUT_PASSWORD = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input" #Пароль при авторизации
    AUTH_BUTTON = By.XPATH, ".//button[text()= 'Войти']" #Кнопка Войти при авторизации
    ORDER_BUTTON = By.XPATH, "//button[text()= 'Оформить заказ']" #Кнопка оформить заказ в конструкторе
    AUTH_LINK = By.XPATH, ".//a[@href= '/login']" #Ссылка Войти в "Уже зарегистрированы" при регистрации
    RESTORE_PASSWORD = By.XPATH, ".//a[@href= '/forgot-password']" #Восстановить пароль в окне входа
    SAUCES_SECTION = By.XPATH, "//span[text()= 'Соусы']" #Раздел Соусы
    SPICY_SAUCE = By.XPATH, "//p[text()= 'Соус Spicy-X']" #Соус Spicy-X
    STUFFING_SECTION = By.XPATH, "//span[text()= 'Начинки']" #Раздел Начинки
    BEEF_METEORITE = By.XPATH, "//p[text()= 'Говяжий метеорит (отбивная)']" #Говяжий метеорит (отбивная)
    BUNS_SECTION = By.XPATH, "//span[text()= 'Булки']" #Раздел Булки
    FLUORESCENT_BUN = By.XPATH, "//p[text()= 'Флюоресцентная булка R2-D3']" #Флюоресцентная булка R2-D3