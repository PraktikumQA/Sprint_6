from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def click_on_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def switch_on_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def action_arrowdown(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def action_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
