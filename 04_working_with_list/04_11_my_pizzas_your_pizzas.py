favorite_pizzas= ['cheese', 'pepporoni','buffalo chicken']
friend_pizzas= favorite_pizzas[:]

favorite_pizzas.append("sausage")
friend_pizzas.append("spinach")

print('My favorite pizzas are:')
for pizza in favorite_pizzas:
    print(f"-{pizza}")

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
        print(f"-{pizza}")
