import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться окончания загрузки страницы")
    def wait_until_loading_done(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class*='Modal_modal__loading']"))
        )

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        self.wait_until_loading_done()
        self.wait_until_visible(locator).click()

    @allure.step("Ввести текст {text} в элемент {locator}")
    def set_text(self, locator, text):
        self.wait_until_visible(locator).send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.wait_until_visible(locator).text

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_until_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться текста {expected} в элементе {locator}")
    def wait_for_text(self, locator, expected):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, expected)
        )

    @allure.step("Перетащить элемент {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент через JavaScript (рекомендация наставника)."""
        element_from = self.wait_until_visible(source_locator)
        element_to = self.wait_until_visible(target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу {url} в новой вкладке")
    def open_in_new_tab(self, url):
        self.driver.switch_to.new_window("tab")
        self.driver.get(url)
        return self.driver.current_window_handle

    @allure.step("Дождаться текста {expected} в элементе {locator}")
    def wait_for_text(self, locator, expected, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected)
        )

    @allure.step("Дождаться выхода с адреса {url}")
    def wait_until_url_not_contains(self, url):
        return WebDriverWait(self.driver, 10).until_not(EC.url_contains(url))

    @allure.step("Запомнить текущее окно")
    def current_window(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на окно {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)