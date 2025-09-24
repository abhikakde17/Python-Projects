
#Define Menu Of The Restaurant 

menu = {
    "Pizza": 200,
    "Pasta":100,
    "Burger":150,
    "Cold Coffee":50,
    "Cold Drink":40,
    "French Fries": 70,
    "Misal Pav": 80
    
}

#Greet
print("..........WELCOME TO CAFE EVENING..........\n\n")

print("What would you like to have?")

print("Pizza : ₹200\nPasta : ₹100\nBurger : ₹150\nCold Coffee : ₹50\nCold Drink : ₹40\nFrench Fries : ₹ 70\nMisal Pav : ₹80\n")
    
order_total = 0

item_1 = input("Please Enter Your Order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
    
else:
    print(f"{item_1} is not avaible now.")
    
another_order = input("Do you want to have something else?: ")
if another_order == "Yes":
    item_2 = input("Enter another order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} is added to your order")
    else:
        print(f"{item_2} is not avaible now.")
else:
    print("Your order will be ready in a few minutes.")
    
    
print(f"The total amount to pay is : {order_total}")