import pytest
from app import app, db
from models import Author

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_author(client):
    response = client.post('/authors/', json={
        'name': 'zzz1',
        'bio': 'penulis novel',
        'birth_date': '1999-01-21'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'zzz1'

def test_get_authors(client):
    response = client.get('/authors/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_author(client):
    response = client.post('/authors/', json={'name': 'zzz2'})
    author_id = response.json['id']
    response = client.get(f'/authors/{author_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'zzz2'

def test_update_author(client):
    response = client.post('/authors/', json={'name': 'test update author'})
    author_id = response.json['id']
    response = client.put(f'/authors/{author_id}', json={'name': 'Updated Author'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Author'

def test_delete_author(client):
    response = client.post('/authors/', json={'name': 'Delete Author'})
    author_id = response.json['id']
    response = client.delete(f'/authors/{author_id}')
    assert response.status_code == 204
    response = client.get(f'/authors/{author_id}')
    assert response.status_code == 404
