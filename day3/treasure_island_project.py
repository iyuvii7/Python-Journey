print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
which_way = input("You're at a cross road. Where do you want to go? Type 'left' or 'right':\n").lower()
if which_way == "left":
    which_way = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across:\n").lower()
    if which_way == "wait":
        which_way = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if which_way == "red":
            print("It's a room full of fire. Game Over.")
        elif which_way == "yellow":
            print("You found the treasure! You Win!")
        elif which_way == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")