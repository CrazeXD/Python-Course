# This is the code for a simple app that will take a food order
# We will use 3 different food items

print("Ｐａｐａ Ｊｏｈｎ＇ｓ Ｐｉｚｚａ")

print(
    '''
    Items:
    1. Cheese Pizza: $3
    2. Peperoni Pizza: $4
    3. Veggie Pizza: $5
    '''
)
print("Type 1, 2, 3, or Done Into the console to add it to the order")

order = ''
cost = 0
done = False
while not done:
    value = input("Enter an item: ")
    if value == '1':
        order += 'Cheese Pizza, '
        cost += 3
    elif value == '2':
        order += "Peperoni Pizza, "
        cost += 4
    elif value == '3':
        order += "Veggie Pizza, "
        cost += 5
    elif value.lower() == "done":
        done = True
    else:
        print("Not an item, please choose one of the options listed below.")
        print("Type 1, 2, 3, or Done Into the console to add it to the order")

print(f"Your order is {order}and the cost is ${cost}")