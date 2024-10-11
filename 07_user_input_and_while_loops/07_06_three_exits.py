#conditional test in the while statement

topping = ""
prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")

#active variable to control loop

max_toppings = 5
toppings_added = 0

while toppings_added < max_toppings:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"  I'll add {topping} to your pizza.")
    toppings_added += 1

#using a break statement

topping = ""

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"  I'll add {topping} to your pizza.")

print("\nThank you for your order!")