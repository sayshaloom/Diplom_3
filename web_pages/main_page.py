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