from flask import Flask

app = Flask(__name__, template_folder='pages')

from routes.main import main_bp
from routes.schedule import schedule_bp

app.register_blueprint(main_bp)
app.register_blueprint(schedule_bp)

if __name__ == '__main__':
    app.run(debug=True)