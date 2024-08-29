from flask import Flask
from models import db
from routes.authors import authors_bp
from routes.books import books_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(authors_bp, url_prefix='/authors')
app.register_blueprint(books_bp, url_prefix='/books')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
