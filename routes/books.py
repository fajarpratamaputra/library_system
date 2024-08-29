from flask import Blueprint, request, jsonify, abort
from models import db, Book, Author

books_bp = Blueprint('books', __name__)

@books_bp.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books]), 200

@books_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.as_dict()), 200

@books_bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not 'title' in data or not 'author_id' in data:
        abort(400, 'Title and author_id are required')
    
    author = Author.query.get(data['author_id'])
    if not author:
        abort(404, 'Author not found')
    
    book = Book(
        title=data['title'],
        description=data.get('description'),
        publish_date=data.get('publish_date'),
        author_id=author.id
    )
    
    db.session.add(book)
    db.session.commit()
    return jsonify(book.as_dict()), 201

@books_bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    
    book.title = data.get('title', book.title)
    book.description = data.get('description', book.description)
    book.publish_date = data.get('publish_date', book.publish_date)
    
    if 'author_id' in data:
        author = Author.query.get(data['author_id'])
        if not author:
            abort(404, 'Author not found')
        book.author_id = author.id
    
    db.session.commit()
    return jsonify(book.as_dict()), 200

@books_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
