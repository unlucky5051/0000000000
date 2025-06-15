from demexam.src.Models.Base import *
from demexam.src.Models.Roles import Roles

class Users(Base):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    name = CharField()
    role_id = ForeignKeyField(Roles)
    status = BooleanField(default=True)  # По умолчанию сотрудник активен

    @classmethod
    def delete_fired_employees(cls):
        # Удаляем всех сотрудников с status=False
        Users.delete().where(Users.status == False).execute()

    class Meta:
        database = mysql_db