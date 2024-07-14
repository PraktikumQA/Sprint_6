class Url:
    URL_HOME_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    URL_ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    URL_DZEN = 'https://dzen.ru/'


class Answers:
    PAYMENT = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    QUANTITY = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    RENT = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    EXTEND_AND_RETURN = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    CHARGER_INCLUDED = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    DELIVERY_AREA = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class Order:
    name = ['Эмануель', 'Креатив']
    surname = ['Зорг', 'Фамильнов']
    address = ['Элементная, 5', 'Самокатная, 3']
    phone = ['79991234567', '89997654321']
    comment = 'Быстрее!!!!111!1'
    order_1 = [name[0], surname[0], address[0], phone[0], comment]
    order_2 = [name[1], surname[1], address[1], phone[1], comment]
    order_success_message = 'Заказ оформлен'