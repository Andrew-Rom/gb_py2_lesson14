from hw14_user import User, load_json, save_json

PATH = 'my_json.json'


class Loger:
    users_list = []
    user_db = {}
    authorized_user = None

    def __init__(self, path):
        self.path = path
        self.user_db = load_json(path)
        for key, value in self.user_db.items():
            self.users_list.append(User(value[0], int(key), value[1]))

    def authorize(self, the_id, name):
        for user in self.__class__.users_list:
            if user.name == name and user.the_id == the_id:
                self.__class__.authorized_user = user
                return user.level
        else:
            raise Exception('Пользователь с такими данными не найден')

    def add_user(self, new_user_name, new_user_id, new_user_level):
        if new_user_level < self.__class__.authorized_user.level:
            raise Exception('Недостаточный уровень доступа')
        else:
            new_user = User(new_user_name, new_user_id, new_user_level)
            self.users_list.append(new_user)
            if str(new_user.the_id) in self.user_db:
                raise Exception('Пользователь с этим ID уже записан в базу')
            else:
                self.user_db[new_user.the_id] = (new_user.name, new_user.level)
                save_json(self.path, self.user_db)


if __name__ == '__main__':
    loger = Loger(PATH)
    # print(f"Уровень доступа: {loger.authorize(1, 'Johnny D')}")
    # loger.add_user('Ivan Petrov', 6, 1)
    print(f"Уровень доступа: {loger.authorize(4, 'Jane Doe')}")
    loger.add_user('Mad Max', 7, 1)
