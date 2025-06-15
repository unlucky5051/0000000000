from demexam.src.Models.Base import *
from demexam.src.Models.Drinks import Drinks
from demexam.src.Models.Foods import Foods
from demexam.src.Models.Shifts import Shifts
from demexam.src.Models.Statuces import Statuces
from demexam.src.Models.Tables import Tables
from demexam.src.Models.Users import Users  # Добавляем импорт Users

class Orders(Base):
    id = PrimaryKeyField()
    count_cliens = IntegerField()
    table_id = ForeignKeyField(Tables)
    drink_id = ForeignKeyField(Drinks)
    food_id = ForeignKeyField(Foods)
    shift_id = ForeignKeyField(Shifts)
    status_id = ForeignKeyField(Statuces)
    user_id = ForeignKeyField(Users)  # Добавляем поле для привязки к пользователю