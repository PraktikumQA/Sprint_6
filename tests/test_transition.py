import allure

from page_object.page_home import HomePage
from page_object.page_dzen import DzenLocators

from constants import Url


class TestHeaderLinkButtons:
    @allure.description('Проверка перехода на страницу Яндекс Дзена через логотип "Яндекс"')
    def test_transition_by_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Url.URL_HOME_PAGE)
        home_page.accept_cookies()
        home_page.click_yandex_logo()
        home_page.switch_on_tab()
        home_page.find_element_located(DzenLocators.DZEN_NEWS_TITLE)
        assert Url.URL_DZEN in driver.current_url

    @allure.description('Проверка перехода на домашнюю страницу сервиса «Самокат» через логотип «Самокат»')
    def test_transition_by_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Url.URL_HOME_PAGE)
        home_page.accept_cookies()
        home_page.click_make_order_button_top()
        home_page.click_scooter_logo()
        assert Url.URL_HOME_PAGE in driver.current_url
