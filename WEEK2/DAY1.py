class Person:

    def __init__(self, name, age , city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def greet(self):
        print("Hello " + self.name + " from " + self.city)

p1 = Person("Nouman", 28, "Lahore", "Pakistan")
p1.greet()



