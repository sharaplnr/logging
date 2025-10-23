import requests
import logging

logger = logging.getLogger(__name__)

BASE_URL = 'https://reqres.in/api'

def test_get_user_list():
    logger.info("Начало теста")

    url = f"{BASE_URL}/users"
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    logger.info(f"GET запрос на {url}")

    response = requests.get(url=url, headers=headers)

    assert response.status_code == 200
    logger.info("Статус код - корректный")
    logger.debug(f"Response body: {response.json()}")

    data = response.json()
    assert "data" in data

    logger.info(f"Получено пользователей: {len(data['data'])}")
    logger.debug(f"Первый пользователь: {data['data'][0]}")
    logger.info("Тест завершен успешно")