import random

# print(help(random))
print(random.randint(1, 6))
print(random.random())

options=("rock","paper","scissors")

option = random.choice(options)
print(option)

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)