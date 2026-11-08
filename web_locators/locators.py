from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    INGREDIENT = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    INGREDIENT_POPUP_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter__num')]")
    BUN_DROP_ZONE = (By.XPATH, "//span[contains(@class, 'constructor-element__text') and contains(text(), 'Перетяните булочку сюда (верх)')]")
