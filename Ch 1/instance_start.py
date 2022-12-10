# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is the secret Attribute."

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_amount"):
            return self.price - self.price * self._amount

        return self.price

    def get_discount(self, amount):
        self._amount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "ankit", 120, 5)
b2 = Book("The Catcher in the Rye", "ram", 130, 7)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.get_discount(0.25)
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter
# __ double score values cannot be accessed in the python outside of class. Its private value.
print(b2._Book__secret)
