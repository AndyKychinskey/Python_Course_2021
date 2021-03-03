from a_kychinskii_s_package.utils.reader import Reader

class Book:
    def __init__( self, ID, title, author, publish_year ):
        self.__id = ID
        self.__title = title
        self.__author = author
        self.__publish_year = publish_year
        self.__reader_s_ID = None

    def __repr__(self):
        return 'ID={}, title="{}", author={}, pub_year={}'.\
            format(self.__id, self.__title, self.__author, self.__publish_year)

    def get_ID(self):
    	return self.__id

    def get_title(self):
    	return self.__title

    def get_author(self):
    	return self.__author

    def get_publish_year(self):
    	return self.__publish_year

    def get_reader_s_ID(self):
    	return self.__reader_s_ID

    def set_reader_s_ID(self, new_ID):
    	self.__reader_s_ID = new_ID
