# # class title:

# #     def __init__(self, title: str):
# #         self.title = title

# # class seat:

# #     def __init__(self, seats: int):
# #         self.seats = seats

# # class row:

# #     def __init__(self, row: int):
# #         self.row = row

# # class screen:

# #     def __init__(self, screen_num: int):
# #         self.screen_num = screen_num

# # class price:

# #     def __init__(self, price: float):
# #         self.price = price

# # class cinema:

# #     def __init(self):
# #         self.movies = [title("terminator"), title("John Wick"), title("Scarface")]
# #         self.screen = [screen(1), screen(2), screen(3)]
# #         self.price = [price(1500), price(3000), price(5000)]
# #         self.row = {}
# #         self.seat= {}

# class student:
#     def  __init__(self, name, father_name, roll_num, class_room):
#         self.name = name
#         self.father_name = father_name
#         self.roll_num = roll_num
#         self.class_room = class_room

#     def my_student(self):
#         print(self.name)
#         print(self.father_name)
#         print(self.class_room)
#         print(self.roll_num)


# # def  __init__(self, name, father_name, roll_num, class_room):
# s1 = student("nouman","Akhtar sb",21,321)
# s2 = student("Dawood","Tariq sb",22,321)

# s2.my_student()

class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year =  year

    def my_car(self):
        print(self.name)
        print(self.model)
        print(self.year)

car1 = car("Audi", "A8", 2022)

car1.my_car()