import math
import re
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):
        """Проверяет наличие кнопки добавления продукта в корзину."""
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Кнопка добавления товара в корзину отсутствует."

    def add_to_basket(self):
        """Добавляет продукт в корзину."""
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def should_be_name(self):
        """Проверяет наличие названия продукта."""
        assert self.is_element_present(*ProductPageLocators.NAME), 'Отсутствует название продукта.'

    def get_product_name(self):
        """Возвращает название продукта."""
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def should_be_price(self):
        """Проверяет наличие цены продукта."""
        assert self.is_element_present(*ProductPageLocators.PRICE), 'Отсутствует цена продукта.'

    def get_product_price(self):
        """Возвращает цену товара."""
        msg = self.browser.find_element(*ProductPageLocators.PRICE).text
        try:
            return float(re.search(r'\d+(\.\d+)?', msg).group(0).replace(',', '.'))
        except AttributeError:
            return 0.0

    def should_be_basket_mini(self):
        """Проверяет наличие суммы цен товаров, добавленных в корзину."""
        assert self.is_element_present(*ProductPageLocators.BASKET_MINI), 'Отсутствует сумма цен товаров, добавленных в корзину.'

    def get_total_price(self):
        """Возвращает сумму цен товаров, добавленных в корзину."""
        msg = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        try:
            return float(re.search(r'\d+(\.\d+)?', msg).group(0).replace(',', '.'))
        except AttributeError:
            return 0.0

    def should_be_msg_product_added_to_basket(self):
        """Проверяет наличие сообщения об успешном добавлении товара в корзину."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET), 'Отсутствует сообщение об успешном добавлении товара в корзину.'

    def get_name_of_product_was_added_to_basket(self):
        """Возвращает название продукта, который был добавлен в корзину."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET).text

    def should_product_added_to_basket(self):
        """Проверяет, добавлен ли текущий продукт в корзину."""
        assert self.get_product_name() == self.get_name_of_product_was_added_to_basket(), 'В корзину добавлен не тот продукт.'

    def should_not_be_success_message(self):
        """Проверяет отсутствие сообщения об успехе."""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Присутствует сообщение об успехе."

    def should_disappear_of_success_message(self):
        """Проверяет, что сообщение об успехе исчезло."""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло."

    def solve_quiz_and_get_code(self):
        """Решает капчу и копирует код в буфер обмена."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
