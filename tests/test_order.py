import pytest

import allure

from page_object.page_order import OrderPage
from page_object.page_home import HomePage, HomePageLocators

from constants import Order


class TestMakeOrder:
    @allure.title('Оформляем заказ')
    @pytest.mark.parametrize('user, button_order', [
        (Order.order_1, HomePageLocators.ORDER_BUTTON_TOP),
        (Order.order_2, HomePageLocators.ORDER_BUTTON_BOTTOM)])
    def test_order(self, driver, user, button_order):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        order_page = OrderPage(driver)
        order_page.make_order(button_order)
        order_page.fill_for_whom_form(user[0], user[1], user[2], user[3])
        order_page.fill_about_rent_form(user[4])
        assert 'Заказ оформлен' in order_page.check_success_order()
