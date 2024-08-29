from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    birth_date = db.Column(db.Date)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bio": self.bio,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None
        }

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    publish_date = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "publish_date": self.publish_date.isoformat() if self.publish_date else None,
            "author_id": self.author_id
        }
