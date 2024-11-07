def make_sandwich(*items):
   
    print("\nI'll make you an amazing sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('ham', 'cheddar cheese', 'lettuce', 'mayo')
make_sandwich('peanut butter', 'grape jelly','banana slices')
make_sandwich('turkey','swiss')