import allure

from web_locators.locators import LoginPageLocators
from web_pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ввести email {email}")
    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку «Войти»")
    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Войти под пользователем {email}")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login()