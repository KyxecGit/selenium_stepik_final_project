from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя.
        :param email: Адрес электронной почты.
        :param password: Пароль.
        """
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()

    def should_be_login_page(self):
        """Проверяет, что на странице присутствуют формы авторизации и регистрации."""
        self._should_be_login_url()
        self._should_be_login_form()
        self._should_be_register_form()

    def _should_be_login_url(self):
        """Проверяет, что текущий URL содержит подстроку 'login'."""
        assert 'login' in self.browser.current_url, 'Подстрока "login" отсутствует в текущем URL браузера.'

    def _should_be_login_form(self):
        """Проверяет наличие формы логина на странице."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует."

    def _should_be_register_form(self):
        """Проверяет наличие формы регистрации на странице."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует."
