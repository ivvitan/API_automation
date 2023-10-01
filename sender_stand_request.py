# Импортируем библиотеку requests
import requests
# Импортируем URL API — Создание заказа и URL API — Получение заказа по номеру трека
from configuration import url_create, url_get


def create_order(order_data):
    # Создание заказа
    response_create = requests.post(url_create, json=order_data)
    return response_create


def get_order(track):
    # Получение информации о заказе по номеру трека
    url = url_get + str(track)
    response_get = requests.get(url)
    return response_get
