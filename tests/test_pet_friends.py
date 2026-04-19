from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


# Получаем api
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

# Смотрим список всех питомцев
def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

# Добавляем нового питомцв
def test_add_new_pet_with_valid_data(name='Филип', animal_type='Бульдог', age='4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # 1. Создаём питомца без фото
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    pet_id = result['id']

    # 2. Добавляем фото к созданному питомцу
    pet_photo = os.path.join(os.path.dirname(__file__), 'images/dog.jpg')
    status, result = pf.add_photo_to_pet(auth_key, pet_id, pet_photo)
    assert status == 200

    # Чистим
    pf.delete_pet(auth_key, pet_id)

# Удаляем питомца
def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Мурзик", "кот", "3", "images/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

# Обновляем данные о питомце
def test_successful_update_self_pet_info(name='Леопольд', animal_type='Киса', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


# Добавление питомца без фото
def test_add_new_pet_simple_with_valid_data(name='Чип', animal_type='хомяк', age='2'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age

    # Удаляем созданного питомца
    pf.delete_pet(auth_key, result['id'])


# Добавление фото к существующему питомцу
def test_add_photo_to_self_pet(pet_photo='images/cat.jpg'):
    """Проверяем возможность добавления фото к своему питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Сначала создаём питомца без фото
    status, new_pet = pf.add_new_pet_simple(auth_key, "Грей", "кот", "3")
    assert status == 200
    pet_id = new_pet['id']

    # Добавляем фото
    status, result = pf.add_photo_to_pet(auth_key, pet_id, pet_photo)

    assert status == 200
    assert result['id'] == pet_id
    assert 'pet_photo' in result

    # Удаляем питомца
    pf.delete_pet(auth_key, pet_id)