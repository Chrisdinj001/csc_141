current_users = ['Greg','Harry','Admin','Justin','Rod']
new_users=['zoey','Bri','JOE','jass','Isabel']

current_users_lower =[user.lower()  for user in current_users]

for new_user in new_users:
    if new_user.lower()in current_users_lower:
        print(f"Sorry {new_user}, this name is taken.")
    
    else:
        print(f"Great, {new_user} is avaliable!")