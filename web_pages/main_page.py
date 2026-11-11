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

    @allure.step("Дождаться значения {expected} у счётчика ингредиента")
    def wait_for_ingredient_counter(self, expected):
        self.wait_for_text(MainPageLocators.INGREDIENT_COUNTER, expected)

    @allure.step("Дождаться окончательного номера заказа в окне")
    def get_order_number(self):
        return self.wait_until_text_stable(MainPageLocators.ORDER_NUMBER)

    @allure.step("Нажать «Оформить заказ»")
    def click_create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_orders_total(self):
        return self.get_text(MainPageLocators.ORDERS_TOTAL_COUNTER)

    @allure.step("Дождаться значения {expected} у счётчика «за всё время»")
    def wait_for_orders_total(self, expected):
        self.wait_for_text(MainPageLocators.ORDERS_TOTAL_COUNTER, expected)

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_orders_today(self):
        return self.get_text(MainPageLocators.ORDERS_TODAY_COUNTER)

    @allure.step("Дождаться значения {expected} у счётчика «за сегодня»")
    def wait_for_orders_today(self, expected):
        self.wait_for_text(MainPageLocators.ORDERS_TODAY_COUNTER, expected)

    @allure.step("Дождаться номера {order_number} в разделе «В работе»")
    def wait_order_in_progress(self, order_number):
        number = f"{int(order_number):05d}"
        return self.wait_for_text(MainPageLocators.IN_PROGRESS_LIST, number, timeout=30)

    @allure.step("Оформить заказ и проверить номер в разделе «В работе»")
    def check_order_in_progress(self, feed_url):
        self.click_create_order()
        order_number = self.get_order_number()
        self.open(feed_url)
        return self.wait_order_in_progress(order_number)