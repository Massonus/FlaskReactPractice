import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from api.models.user import db
from api.config.config import Config
from api.routes.user_routes import user_bp
from api.routes.about_us_routes import about_us_bp

app = Flask(__name__, static_folder='../client/build', static_url_path='/')
app.config.from_object(Config)
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user_bp)
app.register_blueprint(about_us_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
