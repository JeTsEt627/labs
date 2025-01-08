#zadanie1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания {self.year}'

Gogol = Book('Мёртвые души', 'Гоголь', '1835')
print(Book.get_info(Gogol))

#zadanie2
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

Krug = Circle(40)
print(Krug.set_radius(50))
print(Krug.radius)