import os
from flask import Flask, send_from_directory  # Импорт необходимых модулей Flask и os
from flask_cors import CORS  # Импорт CORS для управления кросс-доменными запросами
from api.models.user import db  # Импорт экземпляра базы данных
from api.config.config import Config  # Импорт конфигурации
from api.routes.user_routes import user_bp  # Импорт маршрутов для пользователей
from api.routes.about_us_routes import about_us_bp  # Импорт маршрутов для страницы "О нас"

# Создание экземпляра Flask-приложения
app = Flask(__name__, static_folder='../client/build', static_url_path='/')

# Загрузка конфигурации из объекта Config
app.config.from_object(Config)

# Разрешение кросс-доменных запросов для всего приложения
CORS(app)

# Инициализация базы данных с приложением
db.init_app(app)

# Создание всех таблиц в базе данных
with app.app_context():
    db.create_all()

# Регистрация маршрутов
app.register_blueprint(user_bp)
app.register_blueprint(about_us_bp)


# Обработка маршрутов для React приложения
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    # Если путь существует, отправляем соответствующий файл
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    # Если путь не существует, отправляем index.html
    else:
        return send_from_directory(app.static_folder, 'index.html')


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)  # Включение режима отладки
