from tkinter import *
from src.Controllers.UserController import UserController
from src.Controllers.OrderController import OrderController
from src.Controllers.ShiftController import ShiftController

def admin():
    def status_false(id):
        # Увольняем сотрудника и удаляем его из базы данных
        user.update_status(id)  # Устанавливаем статус "уволен"
        user.delete_fired_employees()  # Удаляем уволенных сотрудников
        update()  # Обновляем интерфейс

    def add_user(login, name, passwd, role):
        user.add(login, passwd, name, role)
        panel_admin.after(1000, update)

    def add_shift(date, cook, oficiant1, oficiant2):
        shift.add(date, cook, oficiant1, oficiant2)
        panel_admin.after(1000, update)

    def update():
        panel_admin.destroy()
        admin()

    panel_admin = Tk()
    panel_admin.geometry('1900x800')
    panel_admin.title("Панель администратора")
    title_window = Label(panel_admin, text="Панель администратора", font=("Times New Roman", 24))
    title_window.grid(column=3, row=0, columnspan=12, padx=400, pady=10)
    title_employee = Label(panel_admin, text="Сотрудники", font=(20))
    title_employee.grid(column=1, row=1, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Роли", font=(20))
    title_employee.grid(column=2, row=1, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Статус", font=(20))
    title_employee.grid(column=3, row=1, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Заказы", font=(20))
    title_employee.grid(column=8, row=1, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Номер столика", font=(20))
    title_employee.grid(column=7, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Количество гостей", font=(20))
    title_employee.grid(column=8, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Блюдо", font=(20))
    title_employee.grid(column=9, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Смены", font=(20))
    title_employee.grid(column=12, row=1, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Дата", font=(20))
    title_employee.grid(column=11, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Повар", font=(20))
    title_employee.grid(column=12, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Официант", font=(20))
    title_employee.grid(column=13, row=2, padx=10, pady=10)
    title_employee = Label(panel_admin, text="Официант", font=(20))
    title_employee.grid(column=14, row=2, padx=10, pady=10)

    shift = ShiftController()
    list_shift = shift.get()
    count_row = 3
    for row in list_shift:
        if row.date:
            date_title = Label(panel_admin, text=row.date)
            date_title.grid(column=11, row=count_row, padx=1, pady=1)
            cook_title = Label(panel_admin, text=row.cook_id.name)
            cook_title.grid(column=12, row=count_row, padx=1, pady=1)
            oficiant1_title = Label(panel_admin, text=row.oficiant_1_id.name)
            oficiant1_title.grid(column=13, row=count_row, padx=1, pady=1)
            oficiant2_title = Label(panel_admin, text=row.oficiant_2_id.name)
            oficiant2_title.grid(column=14, row=count_row, padx=1, pady=1)
        count_row += 1

    order = OrderController()
    list_order = order.get()
    count_row = 3
    for row in list_order:
        if row.table_id:
            table_title = Label(panel_admin, text=row.table_id)
            table_title.grid(column=7, row=count_row, padx=1, pady=1)
            clients_title = Label(panel_admin, text=row.count_cliens)
            clients_title.grid(column=8, row=count_row, padx=1, pady=1)
            food_title = Label(panel_admin, text=row.food_id.name)
            food_title.grid(column=9, row=count_row, padx=1, pady=1)
        count_row += 1

    user = UserController()
    list_user = user.get()
    count_row = 2
    for row in list_user:
        if row.status:  # Отображаем только активных сотрудников
            login_title = Label(panel_admin, text=row.login)
            login_title.grid(column=1, row=count_row, padx=1, pady=1)
            role_title = Label(panel_admin, text=row.role_id.role)
            role_title.grid(column=2, row=count_row, padx=0, pady=1)
            status_title = Label(panel_admin, text="Активен")
            status_title.grid(column=3, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                                 text="Уволить",
                                 height=2, width=8, background='red', foreground='white',
                                 command=lambda id=row.id: status_false(id))
            button_login.grid(column=5, row=count_row, padx=0, pady=1)
        count_row += 1

    input_login = Entry(panel_admin, width=20)
    name_input_login = Label(panel_admin, text="Введите логин")
    name_input_login.grid(column=6, row=2)
    input_login.grid(column=6, row=3)

    input_name = Entry(panel_admin, width=20)
    name_input_name = Label(panel_admin, text="Введите имя")
    name_input_name.grid(column=6, row=4)
    input_name.grid(column=6, row=5)

    input_password = Entry(panel_admin, width=20)
    name_input_password = Label(panel_admin, text="Введите пароль")
    name_input_password.grid(column=6, row=6)
    input_password.grid(column=6, row=7)

    input_role = Entry(panel_admin, width=20)
    name_input_role = Label(panel_admin, text="Введите роль")
    name_input_role.grid(column=6, row=8)
    input_role.grid(column=6, row=9)

    button_add_user = Button(panel_admin, text="Добавить пользователя", height=2, width=20,
                             background='green', foreground='white',
                             command=lambda: add_user(input_login.get(), input_name.get(), input_password.get(),
                                                      input_role.get()))

    button_add_user.grid(column=6, row=10)

    input_datetime = Entry(panel_admin, width=20)
    name_input_datetime = Label(panel_admin, text="Введите дату и время смены")
    name_input_datetime.grid(column=15, row=2)
    input_datetime.grid(column=15, row=3)

    input_cook = Entry(panel_admin, width=20)
    name_input_cook = Label(panel_admin, text="Назначьте повара на смену")
    name_input_cook.grid(column=15, row=4)
    input_cook.grid(column=15, row=5)

    input_oficiant_id = Entry(panel_admin, width=20)
    name_input_oficiant_id = Label(panel_admin, text="Назначьте официанта на смену")
    name_input_oficiant_id.grid(column=15, row=6)
    input_oficiant_id.grid(column=15, row=7)

    input_oficiant_2_id = Entry(panel_admin, width=20)
    name_input_oficiant_2_id = Label(panel_admin, text="Назначьте второго официанта на смену")
    name_input_oficiant_2_id.grid(column=15, row=8)
    input_oficiant_2_id.grid(column=15, row=9)

    button_add_shift = Button(panel_admin, text="Добавить смену", height=2, width=20,
                             background='green', foreground='white',
                             command=lambda: add_shift(input_datetime.get(), input_cook.get(), input_oficiant_id.get(), input_oficiant_2_id.get()))

    button_add_shift.grid(column=15, row=10)

    panel_admin.mainloop()

if __name__ == "__main__":
    admin()