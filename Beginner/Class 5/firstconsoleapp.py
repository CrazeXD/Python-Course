# This is the code for a simple app that will take a food order
# We will use 3 different food items

print("Ｐａｐａ Ｊｏｈｎ＇ｓ Ｐｉｚｚａ")

menu = {"Cheese Pizza": 3, "Pepperoni Pizza": 4, "Veggie Pizza": 5}

for i in range(len(menu)):
    print(f"{i+1}. {list(menu.keys())[i]} - ${list(menu.values())[i]}") #Print out all the menu items
    
print("4. Exit")

a = True
cost = 0
choices = []
while a:
    order = int(input("What would you like to order? "))
    if order == 4:
        a = False
    else:
        choices.append(list(menu.keys())[order-1])
        cost+=list(menu.values())[order-1]

choicestring = ""
for choice in choices:
    choicestring+=f"{choice}, "
print(f"Your order is: {choicestring}and the cost of the order is ${cost}. Thanks for ordering!")
        
    