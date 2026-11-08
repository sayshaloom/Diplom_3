import allure

from data.urls import Urls
from web_pages.main_page import MainPage


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