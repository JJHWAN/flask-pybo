from flask import Blueprint, url_for
from werkzeug.utils import redirect
from pybo.models import Question
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question._list', category_name='qna'))
