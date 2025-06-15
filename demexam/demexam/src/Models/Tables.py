from demexam.src.Models.Base import *

class Tables(Base):
    id = PrimaryKeyField
    number = IntegerField()