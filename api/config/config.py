import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:root@localhost:5432/Test') # URL базы данных, по умолчанию PostgreSQL.
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # отключает трекинг модификаций для экономии ресурсов.
