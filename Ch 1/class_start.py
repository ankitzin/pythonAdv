# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPE = ("Hardcover", "Ebook")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    @classmethod
    def get_booktype(cls):
        return Book.BOOK_TYPE
    # TODO: create a static method
    @staticmethod
    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []

        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title):
        self.title = title


# TODO: access the class attribute


# TODO: Create some book instances
b1 = Book("Title 1")
b2 = Book("Title 2")

# TODO: Use the static method to access a singleton object
thebooks = Book.get_booklist()
thebooks.append(b1)
thebooks.append(b2)

print(thebooks)