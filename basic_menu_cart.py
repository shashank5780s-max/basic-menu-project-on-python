#menu program

menu = {

    "Dosa" : 100,
    "pizza": 450.33333,
    "samosa": 20,
    "juice" : 20.00,
    "Bugger" : 1000.40002
      }
cart = []
total = 0

for key ,value  in menu.items():
    print(f"{key:10} : {value:.2f}")

while True:
    food =input("Enter the food you want to order or 'q' to quit: ")

    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()

for food in cart:
    total +=menu.get(food)
    print(food,end=" ")
print()
print(f"Your total bill is : {total:.2f}")


