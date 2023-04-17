from flask import Blueprint, url_for
from werkzeug.utils import redirect

# Blueprint(블루프린트를 구별하는 이름,모듈명인 'main_views'가 인수로 전달됨 , URL에 대한 기본 경로)
bp = Blueprint('main', __name__, url_prefix='/')
# url_prefix는 'http://127.0.0.1:5000/' 에서 가장 마지막의 '/'에 해당됨

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
