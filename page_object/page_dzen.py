from selenium.webdriver.common.by import By


class DzenLocators:

    DZEN_NEWS_TITLE = (By.XPATH, '//div[@data-testid="floor-title-text" and text()="Новости"]')
