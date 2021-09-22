from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, author_id, genre, in_stock) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre, book.in_stock]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for item in results:
        author = author_repository.select(item['author_id'])
        book = Book(item['title'], author, item['genre'], item['in_stock'], item['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['genre'], result['in_stock'])
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE books SET (title, author_id, genre, in_stock) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.in_stock, book.id]
    run_sql(sql, values)