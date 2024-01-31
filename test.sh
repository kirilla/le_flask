#!/bin/bash

# List all books
curl -X GET http://localhost:3000/books

# Get a book by ID (replace 1 with the actual book ID)
curl -X GET http://localhost:3000/books/1

# Create a new book (modify the JSON payload as necessary)
curl -X POST http://localhost:3000/books -H "Content-Type: application/json" -d '{"title": "New Book", "author": "Author Name"}'

# Update a book (replace 1 with the book ID and modify the JSON payload as necessary)
curl -X PUT http://localhost:3000/books/1 -H "Content-Type: application/json" -d '{"title": "Updated Book Title", "author": "Updated Author Name"}'

# Delete a book (replace 1 with the book ID to delete)
curl -X DELETE http://localhost:3000/books/1
