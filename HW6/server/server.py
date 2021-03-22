import socket
import pickle
import communication
import time
from commands import *
# library files
from lib_files.book import Book
from lib_files.reader import Reader
from lib_files.library import Library

# create library, readers: start
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
# create library, readers: end

_socket = socket.socket()
_socket.bind( (socket.gethostname(), 56+13) )
_socket.listen(1)
_commands = "List of possible commands:\nGET_ALL_BOOKS_IN_LIBRARY\nGET_ALL_AVAILABLE_BOOKS\n\
ADD_NEW_BOOK\nDELETE_BOOK\nGET_ALL_READERS\nTAKE_A_BOOK\nRETURN_A_BOOK\n"
while True:
    clientsocket, address = _socket.accept()
    print(f"Connection from {address} has been established.")
    print(_commands)
    communication.sendMsg( _commands, clientsocket)
    time1 = time.time()
    while True:
        response = communication.readMsg(clientsocket)
        if(response):
            time1 = time.time()
            # handling queries to library from client
            if(response == GET_ALL_BOOKS_IN_LIBRARY):
                print("Ask for all book's list")
                communication.sendMsg( tst_lib.all_books_server_ver(), clientsocket)
            elif(response == GET_ALL_AVAILABLE_BOOKS):
                print("Ask for available books")
                communication.sendMsg(tst_lib.books_in_library_server_ver(), clientsocket)
            elif(response == ADD_NEW_BOOK):
                print("Add a book")
                new_book = communication.readMsg(clientsocket)
                tst_lib.add_book(new_book)
            elif(response == DELETE_BOOK):
                print("Delete a book")
                book_to_delete_ID = communication.readMsg(clientsocket)
                tst_lib.delete_book( int(book_to_delete_ID) )
            elif(response == GET_ALL_READERS):
                print("Ask for all readers")
                communication.sendMsg(tst_lib.return_readers(), clientsocket)
            elif(response == TAKE_A_BOOK):
                print("Take a book")
                book_ID, reader_ID = communication.readMsg(clientsocket)
                tst_lib.give_to_reader_via_IDs(int(book_ID), int(reader_ID))
                print(tst_lib.return_readers())
            elif(response == RETURN_A_BOOK):
                print("Take back a book")
                book_ID, reader_ID = communication.readMsg(clientsocket)
                tst_lib.take_from_reader_via_IDs(int(book_ID), int(reader_ID))
                print(tst_lib.return_readers())
        if(time.time() - time1 > 7):
            clientsocket.close()
            print('Connection closed...')
            break