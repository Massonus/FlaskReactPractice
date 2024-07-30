from flask import Blueprint, jsonify

about_us_bp = Blueprint('about_us_bp', __name__)


@about_us_bp.route('/about-us', methods=['GET'])
def about_us():
    return jsonify({'message': 'This is the About Us page of our application.'})
