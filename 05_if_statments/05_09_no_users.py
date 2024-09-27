usernames=[]

if usernames:
    for username in usernames:
        if username=="admin":
            print("Hello admin, would you like to veiw your status report?")
        else:
            print(f'Hello {username}, welcome back!')

else:
    print("We need to find some users!")