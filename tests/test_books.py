import pytest
from app import app, db
from models import Author, Book

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_book(client):
    response = client.post('/authors/', json={
        'name': 'Tere Liye',
        'bio': 'Novelis',
        'birth_date': '1979-05-21'
    })
    author_id = response.json['id']

    response = client.post('/books/', json={
        'title': 'Hafalan Sholat Delisa',
        'description': 'Hafalan Sholat Delisa',
        'publish_date': '2005-01-01',
        'author_id': author_id
    })
    assert response.status_code == 201
    assert response.json['title'] == 'Hafalan Sholat Delisa'
    assert response.json['author_id'] == author_id

def test_get_books(client):
    response = client.get('/books/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_book(client):

    response = client.post('/authors/', json={'name': 'Andrea Hirata'})
    author_id = response.json['id']

    response = client.post('/books/', json={
        'title': 'Laskar Pelangi',
        'description': 'Laskar Pelangi',
        'publish_date': '2005-01-01',
        'author_id': author_id
    })
    book_id = response.json['id']

    response = client.get(f'/books/{book_id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Laskar Pelangi'
    assert response.json['description'] == 'Laskar Pelangi'
    assert response.json['author_id'] == author_id

def test_update_book(client):
    response = client.post('/authors/', json={'name': 'Update Author'})
    author_id = response.json['id']

    response = client.post('/books/', json={
        'title': 'Original Title',
        'description': 'Original description',
        'publish_date': '2000-01-01',
        'author_id': author_id
    })
    book_id = response.json['id']

    response = client.put(f'/books/{book_id}', json={
        'title': 'Updated Title',
        'description': 'Updated description'
    })
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Title'
    assert response.json['description'] == 'Updated description'

def test_delete_book(client):
    response = client.post('/authors/', json={'name': 'Delete Author'})
    author_id = response.json['id']

    response = client.post('/books/', json={
        'title': 'Delete Book',
        'description': 'This book will be deleted',
        'publish_date': '2000-01-01',
        'author_id': author_id
    })
    book_id = response.json['id']

    response = client.delete(f'/books/{book_id}')
    assert response.status_code == 204

    response = client.get(f'/books/{book_id}')
    assert response.status_code == 404

def test_get_books_by_author(client):
    response = client.post('/authors/', json={'name': 'Author Multiple Books'})
    author_id = response.json['id']

    client.post('/books/', json={
        'title': 'First Book',
        'description': 'The first book by the author',
        'publish_date': '2020-01-01',
        'author_id': author_id
    })

    client.post('/books/', json={
        'title': 'Second Book',
        'description': 'The second book by the author',
        'publish_date': '2021-01-01',
        'author_id': author_id
    })

    response = client.get(f'/authors/{author_id}/books')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['title'] == 'First Book'
    assert response.json[1]['title'] == 'Second Book'
