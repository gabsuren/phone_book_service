from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import db
from flask import Flask
from api.user import user_api
from api.contact import contact_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "Your_secret_string"
app.register_blueprint(user_api)
app.register_blueprint(contact_api)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
