class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        def mov(self):
            print("move")

class Ship(Vehicle):
        def sail(self):
            print("sail")


veh1 = Vehicle("BMW", "M8", 2022)
ship1 = Ship("Yacht", "Yacht", 2026)

for x in (veh1, ship1):
     print(x.brand, x.model, x.year)
     

