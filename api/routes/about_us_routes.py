from flask import Blueprint, jsonify  # Импорт необходимых модулей Flask

# Создание экземпляра Blueprint для маршрутов страницы "О нас"
about_us_bp = Blueprint('about_us_bp', __name__)


# Маршрут для получения информации о странице "О нас"
@about_us_bp.route('/about-us', methods=['GET'])
def about_us():
    return jsonify({'message': 'This is the About Us page of our application.'})  # Возврат сообщения в формате JSON
