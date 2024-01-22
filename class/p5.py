class Publisher:
    def __init__(self, n):
        self.name = n

class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author

    def display(self):
        print("Title:\t", self.title)
        print("Author:\t", self.author)
        print("Name: \t", self.name)

class Python(Book):
    def __init__(self, name, title, author, no_of_pages, price):
        Book.__init__(self, name, title, author)
        self.no_of_pages = no_of_pages
        self.price = price

    def display(self):
        print("Publisher name:\t", self.name)
        print("Title:\t\t", self.title)
        print("Author:\t\t", self.author)
        print("Number of Pages:", self.no_of_pages)
        print("Price.\tRs:", self.price)

# main
p = Python("Penguin", "Hi", "Jith Jolly", 200, 300)
p.display()
