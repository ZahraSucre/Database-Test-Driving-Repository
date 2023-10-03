from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository



# Connect to the database
connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/book_store.sql")
book_repository = BookRepository(connection)

for book in book_repository.all():
    print(book)

book_repository = BookRepository(connection)
