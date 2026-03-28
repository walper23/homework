from flask import Blueprint

schedule_bp = Blueprint('schedule_bp', __name__)

@schedule_bp.route('/schedule')
def schedule():
    return "<h1>Расписание</h1>"

@schedule_bp.route('/schedule/today')
def today():
    return "<h2>Сегодня: пары</h2>"

# ДЗ
@schedule_bp.route('/schedule/tomorrow')
def tomorrow():
    return "<h2>Завтра: отдых</h2>"

@schedule_bp.route('/schedule/week')
def week():
    return "<h2>Неделя: учёба</h2>"