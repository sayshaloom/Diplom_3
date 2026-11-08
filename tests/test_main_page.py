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