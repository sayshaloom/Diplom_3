import allure

from data.test_data import COUNTER_AFTER, COUNTER_BEFORE, POPUP_TITLE
from data.urls import Urls
from web_pages.main_page import MainPage


class TestMainPage:

    @allure.title("Переход в «Конструктор» по клику на кнопку")
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.open(Urls.FEED)
        page.click_constructor()
        assert page.get_current_url() == Urls.MAIN

    @allure.title("Переход в «Ленту заказов» по клику на кнопку")
    def test_click_order_feed(self, main_page):
        main_page.click_order_feed()
        assert main_page.get_current_url() == Urls.FEED

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_popup_opens(self, main_page):
        main_page.click_ingredient()
        assert main_page.get_popup_title() == POPUP_TITLE

    @allure.title("Окно ингредиента закрывается по крестику")
    def test_close_popup_by_cross(self, main_page):
        main_page.click_ingredient()
        main_page.click_close_popup()
        assert main_page.is_popup_closed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases(self, main_page):
        assert main_page.get_ingredient_counter() == COUNTER_BEFORE
        main_page.drag_bun_to_constructor()
        main_page.wait_for_ingredient_counter(COUNTER_AFTER)
        assert main_page.get_ingredient_counter() == COUNTER_AFTER