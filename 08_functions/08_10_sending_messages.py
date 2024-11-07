def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hi, what are you doing?","beautiful day we're having!" "how are u?", "whats your favorite color?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)