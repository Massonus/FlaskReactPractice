from flask import Blueprint, request, jsonify  # Импорт необходимых модулей Flask
from api.models.user import db, User  # Импорт базы данных и модели User

# Создание экземпляра Blueprint для маршрутов пользователей
user_bp = Blueprint('user_bp', __name__)


# Маршрут для получения всех пользователей
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # Получение всех пользователей из базы данных
    return jsonify([user.to_dict() for user in users])  # Возврат списка пользователей в формате JSON


# Маршрут для добавления нового пользователя
@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Получение данных из запроса
    new_user = User(name=data['name'])  # Создание нового пользователя
    db.session.add(new_user)  # Добавление пользователя в сессию базы данных
    db.session.commit()  # Фиксация изменений в базе данных
    return jsonify(new_user.to_dict()), 201  # Возврат данных нового пользователя в формате JSON


# Маршрут для обновления данных пользователя
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()  # Получение данных из запроса
    user = User.query.get(user_id)  # Получение пользователя по ID
    if user:
        user.name = data['name']  # Обновление имени пользователя
        db.session.commit()  # Фиксация изменений в базе данных
        return jsonify(user.to_dict()), 200  # Возврат данных обновленного пользователя в формате JSON
    return jsonify({'message': 'User not found'}), 404  # Возврат ошибки, если пользователь не найден


# Маршрут для удаления пользователя
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)  # Получение пользователя по ID
    if user:
        db.session.delete(user)  # Удаление пользователя из базы данных
        db.session.commit()  # Фиксация изменений в базе данных
        return jsonify({'message': 'User deleted'}), 200  # Возврат подтверждения удаления
    return jsonify({'message': 'User not found'}), 404  # Возврат ошибки, если пользователь не найден
