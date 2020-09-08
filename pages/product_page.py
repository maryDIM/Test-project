import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD_BTN), "Add to basket button isn't presented"

    def add_item_to_basket(self):
        add_item_btn = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BTN)
        add_item_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in basket and in product page isn't equal"

    def should_name_equal(self):
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = ''
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"

    def should_item_in_basket(self):
        self.should_cost_equal()
        self.should_name_equal()