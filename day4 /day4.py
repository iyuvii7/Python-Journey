import random

# Random integer
# random_int = random.randint(1,10)
# print(random_int)

# Random float btween 0 and 1
# random_float = random.random() * 100
# print(random_float)

# # Random float between a and b
# random_float = random.uniform(1,10)
# print(random_float)

# # Create heads and tails
# random_side = random.randint(0, 1)
# # print(random_side)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# Lists

# Who will pay the bill?
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
random_friend = random.choice(friends)
print(f"{random_friend} will pay the bill today!")