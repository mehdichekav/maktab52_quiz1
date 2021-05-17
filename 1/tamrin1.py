import pickle
import os



class Book:

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date

    def __repr__(self):
        return f"{self.ISBN} : {self.name} {self.author} <{self.publisher} > {self.publish_date}"


if os.path.getsize('books.pkl') > 0:
    with open('books.pkl', "+rb") as f:
        unpickler = pickle.load(f)
        print(unpickler)
        x = unpickler.sorted()

