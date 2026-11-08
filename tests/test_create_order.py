import allure

from data.urls import Urls
from web_locators.locators import MainPageLocators
from web_pages.login_page import LoginPage
from web_pages.main_page import MainPage


class TestCreateOrder:

    @allure.title("Счётчики ленты увеличиваются после оформления заказа")
    def test_orders_counters_increase(self, driver, user):
        # 1. Логин под тестовым пользователем
        login_page = LoginPage(driver)
        login_page.open(Urls.LOGIN)
        login_page.login(user["email"], user["password"])

        # 2. Запоминаем счётчики до заказа
        page = MainPage(driver)
        page.open(Urls.FEED)
        total_before = int(page.get_orders_total())
        today_before = int(page.get_orders_today())

        # 3. Собираем бургер и оформляем заказ
        page.open(Urls.MAIN)
        page.drag_bun_to_constructor()
        page.click_create_order()
        order_number = page.get_order_number()
        assert order_number.isdigit()

        # 4. Возвращаемся в ленту и ждём, пока счётчики вырастут
        page.open(Urls.FEED)
        page.wait_for_text(MainPageLocators.ORDERS_TOTAL_COUNTER, str(total_before + 1))
        page.wait_for_text(MainPageLocators.ORDERS_TODAY_COUNTER, str(today_before + 1))

        # 5. Проверяем итоговые значения
        assert int(page.get_orders_total()) == total_before + 1
        assert int(page.get_orders_today()) == today_before + 1