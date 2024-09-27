usernames= ['Greg','Harry','Admin','Justin','Rod']
for username in usernames:
    if username=="admin":
        print("Hello Admin, would you like to veiw your status report?")
    else:
        print(f"Hello {username}, welcome back!")