party_size = input("How many people will there be for your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready.")