from flask import Blueprint, request, jsonify, abort
from models import db, Author, Book

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.as_dict() for author in authors]), 200

@authors_bp.route('/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get_or_404(id)
    return jsonify(author.as_dict()), 200

@authors_bp.route('/', methods=['POST'])
def create_author():
    data = request.get_json()
    if not data or not 'name' in data:
        abort(400, 'Name is required')
    
    author = Author(name=data['name'], bio=data.get('bio'), birth_date=data.get('birth_date'))
    db.session.add(author)
    db.session.commit()
    return jsonify(author.as_dict()), 201

@authors_bp.route('/<int:id>', methods=['PUT'])
def update_author(id):
    data = request.get_json()
    author = Author.query.get_or_404(id)
    
    author.name = data.get('name', author.name)
    author.bio = data.get('bio', author.bio)
    author.birth_date = data.get('birth_date', author.birth_date)
    
    db.session.commit()
    return jsonify(author.as_dict()), 200

@authors_bp.route('/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return '', 204

@authors_bp.route('/<int:id>/books', methods=['GET'])
def get_author_books(id):
    author = Author.query.get_or_404(id)
    return jsonify([book.as_dict() for book in author.books]), 200
