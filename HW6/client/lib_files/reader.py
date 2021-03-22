class Reader:
    def __init__( self, ID, name, surname, age ):
        self.__id = ID
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__book_s_ID = []

    def __repr__(self):
        return 'ID={}, name="{}", surname="{}", age={}, book_s_ID={}'.\
               format(self.__id, self.__name, self.__surname, self.__age, self.__book_s_ID)

    def get_ID(self):
        return self.__id

    def get_name(name):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_book_s_ID(self):
        return self.__book_s_ID

    def add_book_s_ID(self, new_ID):
        self.__book_s_ID.append(new_ID)

    def remove_book_s_ID(self, remove_ID):
        self.__book_s_ID.remove(remove_ID)
