foods = ['mac and cheese', 'potatoes', 'chicken']
friend_foods = foods[:]  # Copy the list

foods.append('alfredo')
friend_foods.append('cookies')

print("My favorite foods are:")
for food in foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")