class Book:
    def init(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print("Kitob:", self.title)
        print("Muallif:", self.author)
        print("Yili:", self.year)


book1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1926)

book1.show_info()