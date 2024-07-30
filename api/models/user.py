from flask_sqlalchemy import SQLAlchemy  # Импорт SQLAlchemy

# Создание экземпляра базы данных
db = SQLAlchemy()


# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Поле ID, является первичным ключом
    name = db.Column(db.String(80), nullable=False)  # Поле имени пользователя, не может быть пустым

    # Метод для преобразования данных пользователя в словарь
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    # Метод to_dict нужен для удобного преобразования объекта модели в формат JSON для передачи данных через API
