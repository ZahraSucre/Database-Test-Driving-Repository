from lib.book import Book


"""
Construct with
    id, title and author_name
"""
def test_construct_with_fields():
    book = Book(4, "Dracula", "Bram Stoker")
    assert book.id == 4
    assert book.title == "Dracula"
    assert book.author_name == "Bram Stoker"

"""
When I construct two Books with the same fields
They are equals
"""
def test_equality():
    book_1 = Book(4, "Dracula", "Bram Stoker")
    book_2 = Book(4, "Dracula", "Bram Stoker")
    assert book_1 == book_2


"""
When I construct a Book
And I format it to a string
Then it comes out in a friendly format
"""
def test_formatting():
    book = Book(4, "Dracula", "Bram Stoker")
    assert str(book) == "Book(4, Dracula, Bram Stoker)"