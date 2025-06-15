from demexam.src.Models.Base import *

class Foods(Base):
    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()