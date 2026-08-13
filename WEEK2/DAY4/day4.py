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


# s1 = student("nouman","Akhtar sb",21,321)
# s2 = student("Dawood","Tariq sb",22,321)

# s2.my_student()

# class car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year =  year

#     def my_car(self):
#          print(self.name, self.model, self.year)
        
# car1 = car("Audi", "A8", 2022)
# car2 = car("BMW", "M8", 2022)

# car1.my_car()
# car2.my_car()

class person:
    def __init__(self, name, f_name, cnic):
        self.name = name
        self.f_name = f_name
        self.cnic = cnic

    def my_display(self):
        print(self.name, self.f_name, self.cnic,) 

class student(person):
    def __init__(self, name, f_name, cnic, department):
        super().__init__(name, f_name, cnic)
        self.department = department

    def my_display(self):
        print(self.name, self.f_name, self.cnic, self.department)        

p1 = person("Nouman", "Akhtar", 35202)
s1 = student("Nouman", "Akhtar", 35202, "Computer Science")

p1.my_display()
s1.my_display()
