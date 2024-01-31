from domain import books


def list_all_books():
    # No need to return status code here as it defaults to 200
    return books.list_all_books()


def get_book_by_id(book_id):
    book = books.get_book_by_id(book_id)
    if book:
        return book
    else:
        return {'message': 'Book not found'}, 404


def create_book(book_data):
    new_book = books.create_book(book_data)
    return new_book, 201


def update_book(book_id, book_data):
    updated_book = books.update_book(book_id, book_data)
    if updated_book:
        return updated_book
    else:
        return {'message': 'Book not found'}, 404
  
  
def delete_book(book_id):
    deleted_book = books.delete_book(book_id)
    if deleted_book:
        return deleted_book
    else:
        return {'message': 'Book not found'}, 404
