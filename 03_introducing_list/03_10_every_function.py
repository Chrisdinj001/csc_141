guests= ['mariah the scientist','gio','teyana taylor','kehlani']

name= guests[0].title()
print(f"{name}, your're invited to my dinner.")

name= guests[1].title()
print(f"{name}, your're invited to my dinner.")

name= guests[2].title()
print(f"{name}, your're invited to my dinner.")

name= guests[3].title()
print(f"{name}, your're invited to my dinner.")

name= guests[3].title()
print(f'\nSorry,{name} cant make it to dinner.')

del(guests[3])
guests.insert(3,"sza")





locations=['bahamas','turks and cacios' ,'dubai','bali','bora bora']

print("Oringinal order:")
print(locations)

print("\nAlaphabetical:")
print(sorted(locations))

print("\nOrignal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOrignal order:")
print(locations)

print("Reversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)


