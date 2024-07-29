import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from api.models.user import db, User
from api.config.config import Config

app = Flask(__name__, static_folder='../client/build', static_url_path='/')
app.config.from_object(Config)
CORS(app)

db.init_app(app)


@app.before_request
def create_tables():
    if not os.path.exists('mydatabase.db'):  # Проверьте, существует ли база данных
        db.create_all()


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
