"""
HW 14
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры
"""

from hw14_user import User
from hw14_logIn import Loger, PATH
import pytest


@pytest.fixture
def data():
    test_name = 'John Doe'
    test_id = 10
    test_level = 5
    return test_name, test_id, test_level


@pytest.fixture
def get_loger():
    return Loger(PATH)


@pytest.fixture
def invalid_name(data):
    test_name, test_id, test_level = data
    test_name = None
    return test_name, test_id, test_level


@pytest.fixture
def invalid_id(data):
    test_name, _, test_level = data
    test_id = -100
    return test_name, test_id, test_level


@pytest.fixture
def invalid_level(data):
    test_name, test_id, _ = data
    test_level = -100
    return test_name, test_id, test_level


@pytest.fixture
def invalid_level(data):
    test_name, test_id, _ = data
    test_level = -100
    return test_name, test_id, test_level


def test_user_creator(data):
    user = User(*data)
    assert user.__str__() == 'John Doe, 10, 5'


def test_invalid_name_exception(invalid_name):
    with pytest.raises(ValueError, match=r'Имя должно быть текстового вида'):
        User(*invalid_name)


def test_invalid_id_exception(invalid_id):
    with pytest.raises(ValueError, match=r'Личный идентификатор должен быть целым числом'):
        User(*invalid_id)


def test_invalid_level_exception(invalid_level):
    with pytest.raises(ValueError, match=r'Уровень доступа должен быть целым числом от 1 до 7'):
        User(*invalid_level)


def test_users_identity(data):
    first_user = User(*data)
    second_user = User(*data)
    second_user.level = second_user.level - 1
    assert first_user == second_user


def test_users_non_identity(data):
    first_user = User(*data)
    second_user = User(*data)
    second_user.the_id = second_user.the_id + 1
    assert first_user != second_user


def test_user_auth(get_loger):
    assert get_loger.authorize(4, 'Jane Doe') == 3


def test_add_user(get_loger):
    get_loger.authorize(4, 'Jane Doe')
    with pytest.raises(Exception, match=r'Недостаточный уровень доступа'):
        get_loger.add_user('Mad Max', 7, 1)


if __name__ == '__main__':
    pytest.main(['-v'])
