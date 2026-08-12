# # div = []
# # for i in range(50):
# #   if(i%2==0) and (i%3!=0):
# #           div.append(i)
# #           print(div)

# ####################

# age = int(input("Enter Age your: "))

# if age >=18:
#     print("You can Enter ")

# elif age <=18:
#     print("Sorry, you can't enter")

# else: age >=25  
# print("Welcome to the Club Mate")

def my_func():
    global like
    like = "Fries"
    print (f"I love {like} very much")

def my_name():
    return f"My name is noman i like {like} very much "

my_func()
print(my_name())
like="Burger"

def change_meal():
    print(f"I like {like} now")

change_meal()