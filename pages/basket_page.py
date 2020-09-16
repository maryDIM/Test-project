
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By



class BasketPage(BasePage):
    def should_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are goods in the box"

    def should_success_message_about_empty_basket(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.ITEM_BASKET)
        assert "Your basket is empty" in empty_basket.text, "There are goods in the box"

