from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template("main.html")

@main_bp.route('/contacts')
def contact():
    return "<h2>Контакты: example@mail.com</h2>"