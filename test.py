# Виталий Ивашов, когорта 8а — Финальный проект. Инженер по тестированию плюс
# Импортируем библиотеку requests
import requests


def test_order_creation_and_retrieval():
    # URL сервера
    server_url = "https://7076c245-0ac1-4981-b2d1-bbbc9c908cd6.serverhub.praktikum-services.ru"
    # URL API — Создание заказа
    url_create = f"{server_url}/api/v1/orders"
    # Данные заказа
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    # Выполнить запрос на создание заказа
    response_create = requests.post(url_create, json=order_data)
    # Сохранить номер трека заказа
    order_track = response_create.json()["track"]
    # Выполнить запрос на получение заказа по треку заказа
    url_get = f"{server_url}/api/v1/orders/track?t={order_track}"
    response_get = requests.get(url_get)
    # Проверить, что код ответа равен 200
    assert response_get.status_code == 200
