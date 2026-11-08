import allure

from web_locators.locators import MainPageLocators
from web_pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Перейти в «Конструктор»")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в «Ленту заказов»")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Получить заголовок окна ингредиента")
    def get_popup_title(self):
        return self.get_text(MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step("Закрыть окно ингредиента крестиком")
    def click_close_popup(self):
        self.click(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step("Проверить, что окно ингредиента закрылось")
    def is_popup_closed(self):
        return self.wait_until_invisible(MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step("Перетащить булочку в конструктор")
    def drag_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BUN_DROP_ZONE)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Дождаться окна с номером заказа и получить номер")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Нажать «Оформить заказ»")
    def click_create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_orders_total(self):
        return self.get_text(MainPageLocators.ORDERS_TOTAL_COUNTER)

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_orders_today(self):
        return self.get_text(MainPageLocators.ORDERS_TODAY_COUNTER)