# # Check the number is even or odd
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You are allowed to ride the roller coster.")
    
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <=18:
        bill = 7
        print("Youth ticket is $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult ticket is $12.")
    
    wants_photo = input("Do you want a photo taken? y or n: ")
    if wants_photo == "y":
        bill += 3
        
    print(f"Your final bill is ${bill}.")
else:
    print("You are not allowed to ride the roller coster.")

# # Pizza Deliveries
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? s, m, or l: ")
# pepperoni = input("Do you want pepperoni? y or n: ")
# extra_cheese = input("Do you want extra cheese? y or n: ")
# bill = 0
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# elif size == "l":
#     bill += 25
# else:
#     print("Invalid size selection.")
# if pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "y":
#     bill += 1
    
# print(f"Your final bill is: ${bill}.")