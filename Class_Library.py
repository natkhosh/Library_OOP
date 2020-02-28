from structure_driver import *
from builder import *
from react import *
from My_LinkedList_Observer import *
from Book import Book



class Library:

    def __init__(self):
        self.__ll = None
        self.__file_lib = None

    @property
    def file_lib(self):
        return self.__file_lib

    @file_lib.setter
    def file_lib(self, file):
        self.__file_lib = file

    def __init_drivers(self):
        print('\n', 'Какой драйвер библиотеки будем использовать:', '\n\t- 1  --> JSON File',
              '\n\t- 2  --> JSON String', '\n\t- 3 --> Pickle Driver', '\n')
        driver_ = None
        choice_ok = False
        while not choice_ok:
            driver_choice = int(input(": > "))
            if driver_choice == 1:
                driver_ = 'json'
                choice_ok = True
            elif driver_choice == 2:
                driver_ = 'json_str'
                choice_ok = True
            elif driver_choice == 3:
                choice_ok = True
                driver_ = 'pickle'
            else:
                print("Не верный выбор")
                choice_ok = False
        structure_driver = SDFabric.get_sd_driver(driver_).build()
        self.__ll = LinkedList(structure_driver)



    def run(self):
        self.__init_drivers()

        # print("Использовать библиотеку по умолчанию или создать новую?",
        #       '\n\t- yes (библиотка поумолчанию)', '\n\t- no (создать новую библиотеку)')
        #
        # file_lib = str(input("> "))
        #
        # if file_lib == 'yes' or file_lib == 'no':
        #     if file_lib == 'yes':
        #         file = "library.txt"
        #     else:
        #         file = str(input('Введите путь библиотеки: >  '))
        # else:
        #     print('Некорректный ввод.', '\n')

        print('\n', 'Список допустимых команд:', '\n\t- add  --> Добавить книгу в библиотеку',
              '\n\t- del  --> Удалить книгу из библиотеку', '\n\t- edit --> Редактировать книгу',
              '\n\t- find --> Поиск книги', '\n\t- exit --> Выход', '\n')
        while True:
            command = str(input("Введите команду: > "))

            if command == 'add' or command == 'del' or command == 'edit' or command == 'find' or command == 'exit':
                if command == 'add':
                    new_book = Book("None", "None", "None")
                    new_book.author = str(input('Введите автора книги: >  '))
                    new_book.title = str(input('Введите название книги: >  '))
                    new_book.year = str(input('Введите год издания книги: >  '))
                    if self.__ll.append(new_book):
                        print('> Книга добавлена', '\n')
                    else:
                        print('> Книга не добавлена', '\n')
                        self.update()

                if command == 'del':
                    del_author = str(input('Введите автора книги: >  '))
                    del_book_name = str(input('Введите название книги: >  '))
                    del_book_year = str(input('Введите год издания книги: >  '))
                    del_book = Book(del_author, del_book_name, del_book_year)
                    self.__ll.remove(del_book)
                    # if add_del_book(file, del_author, del_book_name, del_book_year, 'del'):
                    #     print('> Книга удалена', '\n')
                    # else:
                    #     print('> Книга не удалена', '\n')


                if command == 'edit':
                    add_author = str(input('Введите автора книги: >  '))
                    add_book_name = str(input('Введите название книги: >  '))
                    add_book_year = str(input('Введите год издания книги: >  '))
                    add_author_new = str(input('Введите нового автора книги: >  '))
                    add_book_name_new = str(input('Введите новое название книги: >  '))
                    add_book_year_new = str(input('Введите новый год издания книги: >  '))
                    # if edit_book(file, add_author, add_book_name, add_book_year, add_author_new, add_book_name_new,
                    #              add_book_year_new):
                    #     print('> Книга отредактирована', '\n')
                    # else:
                    #     print('> Книга не отредактирована', '\n')

                if command == 'find':
                    # l = LinkedList()
                    search_ = str(input('Введите поисковый запрос: >  '))
                    search_book = Book(search_, search_, search_)

                    print('Список найденных книг: >  ')
                    print(self.__ll.find(search_book))

                if command == 'exit':
                    break
            else:
                print('Некорректный ввод.', '\nВедите комманду в соотвествии со списком команд.', '\n')

if __name__ == "__main__":

    booklib = Library()
    booklib.run()




