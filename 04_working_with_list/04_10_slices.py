favorite_pizzas = ['cheese', 'pepperoni', 'buffalo chicken','spinach','pesto']


for pizza in favorite_pizzas:
    print(pizza)

print('\n')


for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza.")

print("\nI really love pizza!")

print("\nThe first three items in the list are:")
print(favorite_pizzas[:3])

middle_index = len(favorite_pizzas) // 2
print("\nThree items from the middle of the list are:")
print(favorite_pizzas[middle_index-1:middle_index+2])  # Adjust for middle item

print("\nThe last three items in the list are:")
print(favorite_pizzas[-3:])
