# Library System

Ini adalah API RESTful sederhana untuk mengelola sistem perpustakaan, termasuk menangani operasi yang terkait dengan penulis dan buku. API ini memungkinkan pengguna untuk membuat, mengambil, memperbarui, dan menghapus penulis dan buku, serta mengambil semua buku yang terkait dengan penulis tertentu.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)

## Requirements

To run this application, you will need the following:

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- MySQL database
- Pytest (for testing)
- MySQL client libraries (for Python)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/fajarpratamaputra/library_system.git
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```
## Database Setup

1. **Install MySQL**:  
2. **Create a MySQL database**:
3. **Configure the application to use MySQL**:

    - Open the `config.py` file:

      ```python
      SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://library_user:your_password@localhost/library_db'
      ```

4. **Initialize the database**:  
   Run the following commands to create the necessary tables:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
## Running the Application

1. **Start the Flask development server**:

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

2. **Access the API**:

    - Anda dapat menggunakan alat seperti [Postman](https://www.postman.com/) atau [cURL](https://curl.se/) untuk berinteraksi dengan API.
    - URL dasar untuk API adalah `http://127.0.0.1:5000`.
## API Endpoints

### Authors

- `GET /authors`
- `GET /authors/{id}`
- `POST /authors` 
- `PUT /authors/{id}`
- `DELETE /authors/{id}`
- `GET /authors/{id}/books` 

### Books

- `GET /books` 
- `GET /books/{id}` 
- `POST /books`
- `PUT /books/{id}` 
- `DELETE /books/{id}` 

## Running Tests

```bash
pytest tests/
