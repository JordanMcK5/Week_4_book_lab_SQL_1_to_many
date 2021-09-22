import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Stephen", "King")
author_repository.save(author1)

author2 = Author("Bret", "Easton-Ellis")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("IT", author1, "horror", True)
book_repository.save(book_1)

book_2 = Book("Less Than Zero", author2, "Americana", True)
book_repository.save(book_2)

book_3 = Book("The Shining", author1, "horror", True)
book_repository.save(book_3)

pdb.set_trace()