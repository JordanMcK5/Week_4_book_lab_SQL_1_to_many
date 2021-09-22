class Book:

    def __init__(self, title, author, genre, in_stock = True, id = None,):
        self.title = title
        self.author = author
        self.genre = genre
        self.in_stock = in_stock
        self.id = id

    def mark_in_stock(self):
        self.in_stock = True
