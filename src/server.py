from flask import Flask, jsonify, request, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from controllers import book_controller

app = Flask(__name__)

# Swagger UI configuration
SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.yaml'  # URL for your Swagger specification

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Books API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:path>')
def send_static(path):
    """
    Route for serving static files (like your Swagger specification).
    """
    return send_from_directory('static', path)

# Existing routes

# Route to list all books
@app.route('/books', methods=['GET'])
def list_all_books():
    return jsonify(book_controller.list_all_books())

# Route to get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    return book_controller.get_book_by_id(book_id)

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    return book_controller.create_book(request.json)

# Route to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    return book_controller.update_book(book_id, request.json)

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return book_controller.delete_book(book_id)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
