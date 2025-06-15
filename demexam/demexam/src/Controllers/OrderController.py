from itertools import count

from demexam.src.Models.Orders import *

class OrderController:
    def get(self):
        return Orders.select().execute()

    def add(self, count_cliens, table_id, drink_id, food_id, shift_id, status_id, user_id):
        Orders.create(
            count_cliens=count_cliens,
            table_id=table_id,
            drink_id=drink_id,
            food_id=food_id,
            shift_id=shift_id,
            status_id=status_id,
            user_id=user_id  # Добавляем привязку к пользователю
        )
    def update_order_pay(self,id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_cooking(self, id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_status(self, order_id, new_status_name):
        # Находим статус по имени
        new_status = Statuces.get_or_none(Statuces.name == new_status_name)
        if not new_status:
            return False

        # Обновляем статус заказа
        order = Orders.get_or_none(Orders.id == order_id)
        if order:
            order.status_id = new_status
            order.save()
            return True
        return False

    def delete_order(self, order_id):
        order = Orders.get_or_none(Orders.id == order_id)
        if order:
            order.delete_instance()
            return True
        return False

if __name__ == "__main__":
    sh = OrderController()
    for row in sh.get():
        print(row.id)
    print("---------------")
    sh.add(1,1,1,1,1,1)