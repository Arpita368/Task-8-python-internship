print("ChatBuddy: Hello! I am ChatBuddy 🤖. Type 'bye' to exit.")

while True:
    message = input("Type a message: ")
    if message=="hi" or message=="hello":
        print("\nChatBuddy: Hello! I'm ChatBuddy!")
    elif message=="how are you?":
        print("\nChatBuddy: I'm just a bot, but I'm doing great! How about you?")
        message = input("Type a message: ")
        if message=="good" or message=="fine" or message=="I am good" or message=="i am fine":
            print("\nChatBuddy: Thats nice to hear :)")
        elif message=="bad" or message=="not good":
            print("\nChatBuddy: Ohh... No worries, I wish your day will be good :)")
    elif message=="your name":
        print("\nChatBot: My name is ChatBuddy, your friendly chatbot :) What's your name?")
        name = input("Type a message: ")
        print(f"\nChatBuddy: That's a really nice name :D. Nice to meet you {name}")
    elif message=="weather":
        print("\nChatBuddy: Its raining heavily today. The temperature is 28 degrees in Nanded.")
    elif message=="occasion":
        print("\nChatBuddy: Today is Janmashtami, the day Lord Krishna was born.")
    elif message=="date":
        print("\nChatBuddy: Date: 16 August 2025, Day: Saturday")
    elif message=="help":
        print("\nChatBuddy: Hi, I'm a chatbot, here to help you. Try to ask simple questions like 'how are you?', 'weather', 'occasion', or ask for manual.")
    elif message=="manual":
        print("-----MANUAL-----\n1. hi \n2. hello \n3. how are you?  \n4. your name \n5. weather \n6. occasion \n7. date \n8. help  \n9. manual \n10. nice to meet you \n11. bye")
    elif message=="nice to meet you":
        print("\nChatBuddy: Nice to meet you too :D")
    elif message=="bye":
        print("\nChatBuddy: Goodbye! Have a nice day! :D")
        break
    else:
        print("\nChatBuddy: Sorry, I didn't understand that. Can you try asking differently? or type 'help'")
