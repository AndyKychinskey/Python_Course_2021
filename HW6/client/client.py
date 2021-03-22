import socket
import pickle
import communication
from commands import *
# library files
from lib_files.book import Book
from lib_files.reader import Reader
from lib_files.library import Library

client = socket.socket()
client.connect((socket.gethostname(), 56+13))
# Library commands
commands = communication.readMsg(client)
print(commands)
# take a book
communication.sendMsg( TAKE_A_BOOK, client )
communication.sendMsg( ('6', '1'), client )

# get all readers
communication.sendMsg( GET_ALL_READERS, client )
readers = communication.readMsg(client)
print(readers)

# get all available books
communication.sendMsg( GET_ALL_AVAILABLE_BOOKS, client )
response = communication.readMsg(client)
print(response)

# return a book
communication.sendMsg( RETURN_A_BOOK, client )
communication.sendMsg( ('6', '1'), client )

# get all readers
communication.sendMsg( GET_ALL_READERS, client )
readers = communication.readMsg(client)
print(readers)

# get all books in library
communication.sendMsg( GET_ALL_BOOKS_IN_LIBRARY, client )
response = communication.readMsg(client)
print(response)

# add new book
communication.sendMsg( ADD_NEW_BOOK, client )
communication.sendMsg( Book( 11, "The Call of the Wild", "Jack London", 1903 ), client )

# get all available books
communication.sendMsg( GET_ALL_AVAILABLE_BOOKS, client )
response = communication.readMsg(client)
print(response)

# delete book
communication.sendMsg( DELETE_BOOK, client )
communication.sendMsg( '11', client )
communication.sendMsg( DELETE_BOOK, client )
communication.sendMsg( '10', client )

# get all books in library
communication.sendMsg( GET_ALL_BOOKS_IN_LIBRARY, client )
response = communication.readMsg(client)
print(response)

client.close()