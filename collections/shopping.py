# Shopping cart program
foods=[]
prices=[]
total=0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("_______YOUR CART______")

for food in foods:
    print(food,end=" ")

for price in prices:
    total+=price

print(f"/nThe total price of the foods is ${total}")