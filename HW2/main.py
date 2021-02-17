from library import Library
from book import Book
from reader import Reader

tst_lib = Library( [], [] )

"""
books' data from here:
https://www.penguin.co.uk/articles/2018/100-must-read-classic-books.html
"""

# add books
tst_lib.add_book( Book( 1, "Pride and Prejudice", "Jane Austen", 1813 ) )
tst_lib.add_book( Book( 2, "To Kill a Mockingbird", "Harper Lee", 1960 ) )
tst_lib.add_book( Book( 3, "The Great Gatsby", "F. Scott Fitzgerald", 1925 ) )
tst_lib.add_book( Book( 4, "One Hundred Years of Solitude", "Gabriel García Márquez", 1967 ) )
tst_lib.add_book( Book( 5, "In Cold Blood", "Truman Capote", 1965 ) )
tst_lib.add_book( Book( 6, "Wide Sargasso Sea", "Jean Rhys", 1966 ) )
tst_lib.add_book( Book( 7, "I Capture The Castle", "Dodie Smith", 1948 ) )
tst_lib.add_book( Book( 8, "Jane Eyre", "Charlotte Bronte", 1847 ) )
tst_lib.add_book( Book( 9, "Crime and Punishment", "Fyodor Dostoevsky", 1866 ) )
tst_lib.add_book( Book( 10, "The Secret History", "Donna Tartt", 1992 ) )
# add readers
tst_lib.add_reader( Reader( 1, "Anton", "Skazka", 23 ) )
tst_lib.add_reader( Reader( 2, "Alex", "Berezka", 25 ) )
tst_lib.add_reader( Reader( 3, "Igor", "Talalaev", 30 ) )

tst_lib.all_books()
tst_lib.sort_by_publish_year()
tst_lib.all_books()
tst_lib.sort_by_author()
tst_lib.all_books()
tst_lib.sort_by_title()
tst_lib.all_books()

print( tst_lib.return_books() )
print( tst_lib.return_readers() )

# give book to reader
tst_lib.give_to_reader_via_IDs( 1, 1 )
print( tst_lib.return_readers() )

tst_lib.delete_book( 1 )
print("\nafter .delete_book():")
print( tst_lib.return_readers() )
