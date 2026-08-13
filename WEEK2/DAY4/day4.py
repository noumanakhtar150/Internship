class title:
    def __init__(self, title: str):
        self.title = title

class seat:
    def __init__(self, seats: int):
        self.seats = seats

class row:
    def __init__(self, row: int):
        self.row = row

class screen:
    def __init__(self, screen_num: int):
        self.screen_num = screen_num

class price:
    def __init__(self, price: float):
        self.price = price

class cinema:
    def __init(self):
        self.movies = [title("terminator"), title("John Wick"), title("Scarface")]
        self.screen = [screen(1), screen(2), screen(3)]
        self.price = [price(1500), price(3000), price(5000)]
        self.row = []
        self.seat= []
    def updatePrice(self,newPrice,movieName):
        for movie in self.movies:
            if movie.title == movieName:
                pass

            



print('Ticket Reserved')

