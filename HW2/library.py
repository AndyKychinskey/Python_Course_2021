class Library:
    def __init__( self, Books, Readers ):
        self.__books = Books
        self.__readers = Readers

    def return_books(self):
        return self.__books

    def return_readers(self):
        return self.__readers

    def get_reader_s_index_by_ID( self, ID ):
        for num in range( len( self.__readers ) ):
            if( self.__readers[ num ].get_ID() == ID ):
                return num

    def get_book_s_index_by_ID( self, ID ):
        for num in range( len( self.__books ) ):
            if( self.__books[ num ].get_ID() == ID ):
                return num

    def add_reader( self, reader ):
        self.__readers.append( reader )

    def add_book( self, book ):
        self.__books.append( book )

    def delete_book( self, ID ):
        """
        book_s_num, reader_s_num = self.get_book_s_index_by_ID( ID ), None
        if( self.__books[ book_s_num ].reader_s_ID ):
            reader_s_num = self.get_reader_s_index_by_ID( self.__books[ book_s_num ].reader_s_ID )
            self.take_from_reader( self.__books[ book_s_num ], self.__readers[ reader_s_num ] )
        self.__books.pop( book_s_num )
        """
        # variant 2
        book_s_num, reader_s_num = self.get_book_s_index_by_ID( ID ), None
        just_help_val = self.__books[ book_s_num ]
        if( just_help_val.get_reader_s_ID() ):
            reader_s_num = self.get_reader_s_index_by_ID( just_help_val.get_reader_s_ID() )
            self.take_from_reader( just_help_val, self.__readers[ reader_s_num ] )
        self.__books.pop( book_s_num )

    def give_to_reader( self, book, reader ):
        if( not book.get_reader_s_ID() ):
            reader.add_book_s_ID( book.get_ID() )
            book.set_reader_s_ID( reader.get_ID() )

    def take_from_reader( self, book, reader ):
        if( book.get_reader_s_ID() ):
            reader.remove_book_s_ID( book.get_ID() )
            book.set_reader_s_ID( None )

    def give_to_reader_via_IDs( self, book_ID, reader_ID ):
        self.give_to_reader( self.__books[ self.get_book_s_index_by_ID( book_ID ) ],\
                             self.__readers[ self.get_reader_s_index_by_ID( reader_ID ) ] )

    def take_from_reader_via_IDs( self, book_ID, reader_ID ):
        self.take_from_reader( self.__books[ self.get_book_s_index_by_ID( book_ID ) ],\
                               self.__readers[ self.get_reader_s_index_by_ID( reader_ID ) ] )

    def all_books( self ):
        print( "all books:".upper() )
        for _book in self.__books:
            print( _book )
        print()

    def books_in_library( self ):
        print( "all available books:".upper() )
        for _book in self.__books:
            if( not _book.get_reader_s_ID() ):
                print( _book )
        print()

    def books_used_by_users( self ):
        print( "all current used books:".upper() )
        for _book in self.__books:
            if( _book.get_reader_s_ID() ):
                print( _book )
        print()

    def sort_by_title( self ):
        print( "sorted by title".upper() )
        self.__books = sorted( self.__books, key = lambda book : book.get_title(), reverse = False )

    def sort_by_author( self ):
        print( "sorted by author".upper() )
        self.__books = sorted( self.__books, key = lambda book : book.get_author(), reverse = False )

    def sort_by_publish_year( self ):
        print( "sorted by publish year".upper() )
        self.__books = sorted( self.__books, key = lambda book : book.get_publish_year(), reverse = False )
