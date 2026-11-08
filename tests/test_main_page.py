import allure

from data.urls import Urls
from web_pages.main_page import MainPage
from web_locators.locators import MainPageLocators


class TestMainPage:

    @allure.title("Переход в «Конструктор» по клику на кнопку")
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.open(Urls.FEED)
        page.click_constructor()
        assert driver.current_url == Urls.MAIN

    @allure.title("Переход в «Ленту заказов» по клику на кнопку")
    def test_click_order_feed(self, driver):
        page = MainPage(driver)
        page.open(Urls.MAIN)
        page.click_order_feed()
        assert driver.current_url == Urls.FEED

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_popup_opens(self, driver):
        page = MainPage(driver)
        page.open(Urls.MAIN)
        page.click_ingredient()
        assert page.get_popup_title() == "Детали ингредиента"

    @allure.title("Окно ингредиента закрывается по крестику")
    def test_close_popup_by_cross(self, driver):
       page = MainPage(driver)
       page.open(Urls.MAIN)
       page.click_ingredient()
       page.click_close_popup()
       assert page.is_popup_closed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open(Urls.MAIN)
        assert page.get_ingredient_counter() == "0"
        page.drag_bun_to_constructor()
        page.wait_for_text(MainPageLocators.INGREDIENT_COUNTER, "2")
        assert page.get_ingredient_counter() == "2"  