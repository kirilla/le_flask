class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

# This will act as our in-memory database for simplicity
books_db = [
    Book(1, "Example Book One", "Author A"),
    Book(2, "Example Book Two", "Author B")
]

def list_all_books():
    return [book.__dict__ for book in books_db]


def get_book_by_id(book_id):
    for book in books_db:
        if book.id == book_id:
            return book.__dict__
    return None



def create_book(book_data):
    new_book_id = max(book.id for book in books_db) + 1
    new_book = Book(new_book_id, book_data['title'], book_data['author'])
    books_db.append(new_book)
    return new_book.__dict__



def update_book(book_id, book_data):
    for book in books_db:
        if book.id == book_id:
            book.title = book_data.get('title', book.title)
            book.author = book_data.get('author', book.author)
            return book.__dict__
    return None



def delete_book(book_id):
    global books_db
    book_to_delete = next((book for book in books_db if book.id == book_id), None)
    if book_to_delete:
        books_db = [book for book in books_db if book.id != book_id]
        return book_to_delete.__dict__
    return None
