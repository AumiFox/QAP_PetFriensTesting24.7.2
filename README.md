# QAP_PetFriensTesting24.7.2

Практика 24.7.2


Описание проекта:
Проект содержит автоматизированные тесты для API сервиса PetFriends (https://petfriends.skillfactory.ru/).  
Тесты проверяют основные функции работы с питомцами: получение ключа API, добавление, удаление, обновление информации о питомцах, а также добавление фото.

Технологии
- Python 3
- pytest
- requests
- requests-toolbelt

Установка и запуск

1.Установка зависимостей
bash
pip install -r requirements.txt

2.Настройка

В файле settings.py укажите ваши данные:
import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

В файле.env
valid_email=Test001@mail.ru
valid_password=test1234
test_photo_cat=cat.jpg
test_photo_dog=dog.jpg

4. Создание тестового изображения
В папке tests/images/ разместите файл dog.jpg и cat.jpg

Список тестов

test_get_api_key_for_valid_user	- Получение API ключа по email и паролю
test_get_all_pets_with_valid_key	- Получение списка всех питомцев
test_add_new_pet_with_valid_data	- Добавление нового питомца с фото
test_successful_delete_self_pet	- Удаление своего питомца
test_successful_update_self_pet_info	- Обновление информации о питомце
test_add_new_pet_simple_with_valid_data	- Добавление питомца без фото
test_add_photo_to_self_pet	- Добавление фото к существующему питомцу


