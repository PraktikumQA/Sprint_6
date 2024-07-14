import pytest

import allure

from page_object.page_home import HomePage
from constants import *


class TestFAQ:
    @allure.title('Тестирование ответов на вопросы')
    @pytest.mark.parametrize('question_number, answer_number, answer_text',
        [
            (0, 0, Answers.PAYMENT),
            (1, 1, Answers.QUANTITY),
            (2, 2, Answers.RENT),
            (3, 3, Answers.ORDER_TODAY),
            (4, 4, Answers.EXTEND_AND_RETURN),
            (5, 5, Answers.CHARGER_INCLUDED),
            (6, 6, Answers.CANCEL_ORDER),
            (7, 7, Answers.DELIVERY_AREA)
        ]
    )
    def test_click_on_faq_questions(self, driver, question_number, answer_number, answer_text):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.scroll_to_questions()
        home_page.click_on_question(question_number)
        answer = home_page.get_answer(answer_number)
        assert answer.is_displayed() and answer.text == answer_text
