import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
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

    @allure.step("Перетащить элемент {source} в {target}")
    def drag_and_drop(self, source, target):
        source_element = self.wait_until_visible(source)
        target_element = self.wait_until_visible(target)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step("Дождаться текста {expected} в элементе {locator}")
    def wait_for_text(self, locator, expected):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, expected))