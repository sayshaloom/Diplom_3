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