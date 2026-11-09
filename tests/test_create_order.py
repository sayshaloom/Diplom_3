import allure

from data.test_data import COUNTER_AFTER
from data.urls import Urls
from web_pages.login_page import LoginPage
from web_pages.main_page import MainPage


class TestCreateOrder:

    @allure.title("Счётчики ленты увеличиваются после оформления заказа")
    def test_orders_counters_increase(self, driver, user):
        # 1. Вход под тестовым пользователем
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
        page.wait_for_ingredient_counter(COUNTER_AFTER)
        page.click_create_order()
        order_number = page.get_order_number()
        assert order_number.isdigit()

        # 4. Возвращаемся в ленту и ждём обновления счётчиков
        page.open(Urls.FEED)
        page.wait_for_orders_total(str(total_before + 1))
        page.wait_for_orders_today(str(today_before + 1))

        # 5. Итоговая проверка
        assert int(page.get_orders_total()) == total_before + 1
        assert int(page.get_orders_today()) == today_before + 1

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver, user):
        login_page = LoginPage(driver)
        login_page.open(Urls.LOGIN)
        login_page.login(user["email"], user["password"])

        page = MainPage(driver)
        page.open(Urls.MAIN)
        page.drag_bun_to_constructor()
        page.wait_for_ingredient_counter(COUNTER_AFTER)

        main_window = driver.current_window_handle
        feed_window = page.open_in_new_tab(Urls.FEED)

        driver.switch_to.window(main_window)
        page.click_create_order()
        order_number = page.get_order_number()

        driver.switch_to.window(feed_window)
        page.wait_order_in_progress(order_number)