from weakref import ref
from react import *


class Book(WeakSubject):
    def __init__(self, author, title, year):
        super().__init__()
        self.is_valid_book(author, title, year)
        self.__author = author
        self.__title = title
        self.__year = year

    def __str__(self):
        return f'{self.__author} {self.__title} {self.__year}'

    @classmethod
    def is_valid_book(cls, author, title, year):
        if not isinstance(author, str):
            raise TypeError('author must be string')
        if not isinstance(title, str):
            raise TypeError('title must be string')
        if not isinstance(year, str):
            raise TypeError('year must be string')

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, name):
        name = str(name)
        self.is_valid_book(name, self.__title, self.__year)
        self.__author = name
        self.notify()

    @title.setter
    def title(self, value):
        value = str(value)
        self.is_valid_book(self.__author, value, self.__year)
        self.__title = value
        self.notify()

    @year.setter
    def year(self, value):
        value = str(value)
        self.is_valid_book(self.__author, self.__title, value)
        self.__year = value
        self.notify()

