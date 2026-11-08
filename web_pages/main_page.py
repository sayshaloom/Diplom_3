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