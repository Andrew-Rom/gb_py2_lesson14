import json
import os


class User:
    def __init__(self, name: str, the_id: int, level: int):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть целым числом от 1 до 7')
        self.level = level

    def __eq__(self, other):
        return self.the_id == other.the_id

    def __str__(self):
        return f'{self.name}, {self.the_id}, {self.level}'


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('Введите личный идентификатор: '))
            level = int(input('Введите уровень доступа: '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def save_json(path, user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    path = 'my_json.json'
    user_db = load_json(path)
    new_user = worker()
    if str(new_user.the_id) in user_db:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        user_db[new_user.the_id] = (new_user.name, new_user.level)
        save_json(path, user_db)
