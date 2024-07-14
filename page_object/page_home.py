import allure

from selenium.webdriver.common.by import By

from page_object.page_base import BasePage


# я понимаю что локаторы можно вынести в отдельный файл, но я решил сделать так, как нам показывал наставник.
class HomePageLocators:
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    ACCEPT_COOKIES_BUTTON = (By.ID, 'rcc-confirm-button')
    FAQ_TITLE = (By.XPATH, ".//div[text()='Вопросы о важном']")
    QUESTIONS = (By.XPATH, ".//div[contains(@id, 'accordion__heading')]")
    ANSWERS = (By.XPATH, ".//div[contains(@id, 'accordion__panel')]/p")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        return self.find_element_located(HomePageLocators.ACCEPT_COOKIES_BUTTON).click()

    @allure.step("Нажать на лого Яндекса")
    def click_yandex_logo(self):
        return self.find_element_located(HomePageLocators.YANDEX_LOGO).click()

    @allure.step("Нажать на лого самоката")
    def click_scooter_logo(self):
        return self.find_element_located(HomePageLocators.SCOOTER_LOGO).click()

    @allure.step("Открываем форму заказа нажатием на кнопку «Заказать» вверху страницы")
    def click_make_order_button_top(self):
        self.find_element_located(HomePageLocators.ORDER_BUTTON_TOP).click()

    @allure.step("Открываем форму заказа нажатием на кнопку «Заказать» внизу страницы")
    def click_make_order_button_bottom(self):
        self.find_element_located(HomePageLocators.ORDER_BUTTON_BOTTOM).click()

    def scroll_to_questions(self):
        faq_title = self.find_element_located(HomePageLocators.FAQ_TITLE)
        return self.driver.execute_script("arguments[0].scrollIntoView();", faq_title)

    def scroll_to_make_order_button_bottom(self):
        order_button = self.find_element_located(HomePageLocators.ORDER_BUTTON_BOTTOM)
        return self.driver.execute_script("arguments[0].scrollIntoView();", order_button)

    @allure.step("Кликнуть на вопрос")
    def click_on_question(self, index):
        questions = self.find_elements_located(HomePageLocators.QUESTIONS)
        return questions[index].click()

    @allure.step("Получить ответ")
    def get_answer(self, index):
        answers = self.find_elements_located(HomePageLocators.ANSWERS)
        return answers[index]
