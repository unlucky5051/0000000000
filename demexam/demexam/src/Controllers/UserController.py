from demexam.src.Models.Users import *

class UserController:
    def log_in(self, input_login, input_password):
        user = Users.get_or_none(Users.login == input_login, Users.password == input_password)
        if user:
            return user  # Возвращаем объект пользователя (включая его статус)
        else:
            return None  # Если пользователь не найден
    def get(self):
        return Users.select().execute()

    def add(self, login, password, name, role_id):
        try:
            Users.create(
                login=login,
                password=password,
                name=name,
                role_id=role_id
            )
            print("Сотрудник успешно добавлен!")  # Логируем успешное добавление
        except Exception as e:
            print("Ошибка в UserController.add:", str(e))  # Логируем ошибку
            raise e

    def update_status(self, id_user):
        # Устанавливаем статус "уволен"
        Users.update({Users.status: False}).where(Users.id == id_user).execute()  # Используем execute()
    @classmethod
    def show(cls, identifier):
        # Проверяем, является ли identifier числом (ID)
        if isinstance(identifier, int) or (isinstance(identifier, str) and identifier.isdigit()):
            return Users.get_or_none(Users.id == int(identifier))
        # Иначе ищем по логину
        return Users.get_or_none(Users.login == identifier)

    @classmethod
    def show_user(cls, role_id):
        return Users.select().where(Users.role_id == role_id)

    @classmethod
    def list_user(cls,role_id):
        list= []
        for user in UserController.show_user(role_id):
            list.append(user.login)
        return list



if __name__ == "__main__":
    print(UserController.show('admin_Ekaterina').role.id)