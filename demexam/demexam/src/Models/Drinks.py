from demexam.src.Models.Base import *

class Drinks(Base):
    id = PrimaryKeyField()
    name = CharField()  # Название напитка
    price = DecimalField()  # Цена напитка