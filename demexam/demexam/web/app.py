from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from demexam.src.Controllers.ShiftController import *
from demexam.src.Controllers.UserController import *
from demexam.src.Controllers.OrderController import *
from demexam.src.Models.Users import Users  # Импортируем модель Users
from demexam.src.Models.Shifts import Shifts  # Импортируем модель Shifts
from demexam.src.Models.Orders import Orders  # Импортируем модель Orders
from demexam.src.Models.Statuces import Statuces  # Импортируем модель Statuces
from demexam.src.Models.Foods import Foods  # Импортируем модель Foods
from demexam.src.Models.Drinks import Drinks  # Импортируем модель Drinks
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для сессий

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, user_id, role_id):
        self.id = user_id
        self.role_id = role_id  # Добавляем атрибут role_id


@login_manager.user_loader
def load_user(user_id):
    user = Users.get_or_none(Users.id == user_id)  # Используем модель Users
    if user:
        return User(user_id, user.role_id.id)  # Передаем role_id в объект User
    return None


@app.route('/')  # Главная страница теперь доступна по корневому URL
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user_controller = UserController()
        user = user_controller.log_in(login, password)  # Получаем объект пользователя

        if user:
            # Проверяем статус сотрудника (status == False означает уволен)
            if not user.status:
                flash('Данный сотрудник уволен и не может войти в систему', 'error')
                return render_template('login.html')

            login_user(User(user.id, user.role_id.id))  # Создаем объект User с role_id

            # Определяем роль пользователя и перенаправляем на соответствующую панель
            if user.role_id.id == 1:  # Администратор
                return redirect(url_for('paneladmin'))
            elif user.role_id.id == 2:  # Повар
                return redirect(url_for('panelcook'))
            elif user.role_id.id == 3:  # Официант
                return redirect(url_for('waiterpanel'))
            elif user.role_id.id == 4:  # Обычный пользователь
                return redirect(url_for('userpanel'))
            else:
                flash('Неизвестная роль', 'error')
        else:
            flash('Неверный логин или пароль', 'error')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        name = request.form['name']
        role_id = 4  # Все новые пользователи получают роль "Пользователь" (ID = 4)

        user_controller = UserController()
        try:
            user_controller.add(login, password, name, role_id)
            flash('Регистрация прошла успешно! Пожалуйста, войдите.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Ошибка регистрации: {str(e)}', 'error')

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/paneladmin')
@login_required
def paneladmin():
    if current_user.role_id != 1:  # Предположим, что role_id для администратора равен 1
        return redirect(url_for('home'))
    orders = Orders.select()
    shifts = Shifts.select()
    users = Users.select().where(Users.status == True)  # Отображаем только активных сотрудников
    return render_template('adminpanel.html', orders=orders, shifts=shifts, users=users)


@app.route('/add_employee', methods=['POST'])
@login_required
def add_employee():
    if current_user.role_id != 1:
        return redirect(url_for('home'))

    # Получаем данные из формы
    data = request.get_json()  # Используем request.get_json() для JSON-данных
    login = data.get('login')
    password = data.get('password')
    name = data.get('name')
    role_id = data.get('role_id')

    if not login or not password or not name or not role_id:
        return jsonify({'success': False, 'error': 'Не все данные предоставлены'})

    user_controller = UserController()
    user_controller.add(login, password, name, role_id)
    return jsonify({'success': True})


@app.route('/fire_employee/<int:user_id>', methods=['POST'])
@login_required
def fire_employee(user_id):
    if current_user.role_id != 1:
        return redirect(url_for('home'))

    user_controller = UserController()
    user_controller.update_status(user_id)  # Устанавливаем статус "уволен"

    flash('Сотрудник успешно уволен!', 'success')
    return redirect(url_for('paneladmin'))


@app.route('/add_shift', methods=['POST'])
@login_required
def add_shift():
    if current_user.role_id != 1:
        return redirect(url_for('home'))

    # Получаем данные из формы
    data = request.get_json()  # Используем request.get_json() для JSON-данных
    datetime = data.get('datetime')
    cook = data.get('cook')
    oficiant_1 = data.get('oficiant_1')
    oficiant_2 = data.get('oficiant_2')

    if not datetime or not cook or not oficiant_1 or not oficiant_2:
        return jsonify({'success': False, 'error': 'Не все данные предоставлены'})

    shift_controller = ShiftController()
    shift_controller.add(datetime, cook, oficiant_1, oficiant_2)
    return jsonify({'success': True})


@app.route('/panelcook')
@login_required
def panelcook():
    if current_user.role_id != 2:  # Предположим, что role_id для повара равен 2
        return redirect(url_for('home'))

    # Получаем только заказы, у которых статус НЕ "Отдан" и НЕ "Готов"
    orders = (Orders.select()
              .join(Statuces)
              .where((Statuces.name != "Отдан") & (Statuces.name != "Готов")))

    return render_template('cookpanel.html', orders=orders)


@app.route('/update_order_status/<int:order_id>', methods=['POST'])
@login_required
def update_order_status(order_id):
    if current_user.role_id != 2:  # Только повар может изменять статус заказа
        return jsonify({'success': False, 'error': 'Доступ запрещен'})

    data = request.get_json()
    new_status = data.get('status')

    # Логика обновления статуса заказа
    order = Orders.get_or_none(Orders.id == order_id)
    if order:
        status = Statuces.get(Statuces.name == new_status)
        if status:
            order.status_id = status
            order.save()
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Неверный статус'})
    else:
        return jsonify({'success': False, 'error': 'Заказ не найден'})


@app.route('/waiterpanel')
@login_required
def waiterpanel():
    if current_user.role_id != 3:  # Только для официантов
        return redirect(url_for('home'))

    # Получаем статус "Отдан"
    delivered_status = Statuces.get_or_none(Statuces.name == 'Отдан')

    # Фильтруем заказы - показываем только те, у которых статус не "Отдан"
    if delivered_status:
        orders = Orders.select().where(Orders.status_id != delivered_status.id)
    else:
        orders = Orders.select()

    foods = Foods.select()
    drinks = Drinks.select()
    statuses = Statuces.select()
    return render_template('waiterpanel.html', foods=foods, drinks=drinks, orders=orders, statuses=statuses)

@app.route('/update_order_status_waiter/<int:order_id>', methods=['POST'])
@login_required
def update_order_status_waiter(order_id):
    if current_user.role_id != 3:
        return jsonify({'success': False, 'error': 'Доступ запрещен'})

    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'error': 'Неверный формат данных'})

    new_status = data.get('status')
    if not new_status:
        return jsonify({'success': False, 'error': 'Статус не указан'})

    try:
        order = Orders.get_or_none(Orders.id == order_id)
        if not order:
            return jsonify({'success': False, 'error': 'Заказ не найден'})

        status = Statuces.get_or_none(Statuces.name == new_status)
        if not status:
            return jsonify({'success': False, 'error': 'Неверный статус'})

        order.status_id = status
        order.save()

        return jsonify({
            'success': True,
            'status': new_status,
            'message': f'Статус успешно изменен на "{new_status}"'
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/userpanel')
@login_required
def userpanel():
    if current_user.role_id != 4:  # Только пользователь (роль 4) может получить доступ
        return redirect(url_for('home'))
    foods = Foods.select()
    drinks = Drinks.select()
    orders = Orders.select().where(Orders.user_id == current_user.id)  # Фильтруем заказы по пользователю
    return render_template('userpanel.html', foods=foods, drinks=drinks, orders=orders)


@app.route('/create_order', methods=['POST'])
@login_required
def create_order():
    if current_user.role_id != 4:  # Только пользователь (роль 4) может создавать заказы
        return jsonify({'success': False, 'error': 'Доступ запрещен'})

    table_id = request.json.get('table_id')
    food_id = request.json.get('food_id')
    drink_id = request.json.get('drink_id')

    # Логика создания заказа
    order_controller = OrderController()
    order_controller.add(
        count_cliens=1,  # Пример: 1 клиент
        table_id=table_id,
        drink_id=drink_id,
        food_id=food_id,
        shift_id=1,  # Пример: смена с ID 1
        status_id=1,  # Пример: статус "Новый"
        user_id=current_user.id  # Привязываем заказ к текущему пользователю
    )

    return jsonify({'success': True})


@app.route('/delete_order/<int:order_id>', methods=['POST'])
@login_required
def delete_order(order_id):
    if current_user.role_id != 3:  # Только официант может удалять заказы
        return jsonify({'success': False, 'error': 'Доступ запрещен'})

    # Логика удаления заказа
    order = Orders.get_or_none(Orders.id == order_id)
    if order:
        order.delete_instance()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Заказ не найден'})


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/shifts')
def shifts():
    return render_template('shifts.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')