import allure

from selenium.webdriver.common.by import By
from page_object.page_home import HomePage


# я понимаю что локаторы можно вынести в отдельный файл, но я решил сделать так, как нам показывал наставник.
class OrderPageLocators:
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    STATION_LST = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    RENTAL_START_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_CALENDAR_DATES = (By.XPATH, ".//div[@role='button']")
    RENTAL_PERIOD_INPUT = (By.XPATH, ".//div[text()='* Срок аренды']")
    RENT_PERIOD_DAY = (By.XPATH, '//div[text()="сутки"]')
    SCOOTER_BLACK_COLOUR_CHECKBOX = (By.ID, "black")
    SCOOTER_GREY_COLOUR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]')

    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER_MESSAGE = (By.XPATH, ".//div[text()='Заказ оформлен']")


class OrderPage(HomePage):
    @allure.step("Нажать на кнопку «Заказать»")
    def make_order(self, button_order):
        self.click_on_element(button_order)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.SURNAME_INPUT, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбор станции метро')
    def set_metro(self):
        self.click_on_element(OrderPageLocators.STATION_INPUT)
        self.action_arrowdown()
        self.action_enter()

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_for_whom_form(self, name, last_name, address, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro()
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Выбор даты доставки')
    def set_date(self):
        self.click_on_element(OrderPageLocators.RENTAL_START_DATE_INPUT)
        self.action_arrowdown()
        self.action_enter()

    @allure.step('Выбор продолжительности срока аренды')
    def set_period_rent(self):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_INPUT)
        self.click_on_element(OrderPageLocators.RENT_PERIOD_DAY)

    @allure.step('Выбор цвета чёрный жемчуг')
    def set_color(self):
        self.click_on_element(OrderPageLocators.SCOOTER_BLACK_COLOUR_CHECKBOX)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.COMMENT_INPUT, comments)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_about_rent_form(self, comments):
        self.set_date()
        self.set_period_rent()
        self.set_color()
        self.set_comments(comments)
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Появление всплывающего окна "Заказ оформлен"')
    def check_success_order(self):
        return self.find_element_located(OrderPageLocators.SUCCESS_ORDER_MESSAGE).text
