name_prompt = "\nWhat's your name? "
place_prompt = "Where is you dream vacation? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    #ask the user where they'd want to go.
    name = input(name_prompt)
    place = input(place_prompt)

    #store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

#show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")