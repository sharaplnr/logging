import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__)


def test_successful_login(page: Page):
    """Тест успешной авторизации"""
    logger.info("Начало теста")

    # Переход на страницу
    url = "https://the-internet.herokuapp.com/login"
    logger.info(f"Переход на страницу: {url}")
    page.goto(url)
    logger.debug(f"URL страницы: {page.url}")
    logger.debug(f"Заголовок: {page.title()}")

    # Ввод учетных данных
    logger.info("Заполнение формы авторизации")
    username = "tomsmith"
    password = "SuperSecretPassword!"

    page.fill("#username", username)
    logger.debug(f"Введен логин: {username}")

    page.fill("#password", password)
    logger.debug("Введен пароль: ********")

    # Клик по кнопке входа
    logger.info("Клик по кнопке 'Login'")
    page.click("button[type='submit']")

    # Проверка успешного входа
    logger.info("Проверка успешной авторизации")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    logger.info(f"✓ Успешное перенаправление на: {page.url}")

    # Проверка сообщения об успехе
    success_message = page.locator("#flash")
    expect(success_message).to_be_visible()
    message_text = success_message.inner_text()
    logger.debug(f"Текст сообщения: {message_text}")

    assert "You logged into a secure area" in message_text
    logger.info("Отображается сообщение об успешном входе")

    # Проверка кнопки logout
    logout_button = page.locator("a[href='/logout']")
    expect(logout_button).to_be_visible()
    logger.info("Кнопка 'Logout' отображается")

    logger.info("Тест завершен успешно")