# Basic Rule-Based Chatbot

print(" Chatbot: Hello! Type 'bye' to exit.")

while True:
    # Take user input
    user_input = input("You: ").lower()

    # Check user input and respond
    if user_input in ["hello","hi","hey","ram ram "]:
        print(" Chatbot: Hi there!")
    
    elif user_input == "how are you":
        print(" Chatbot: I'm doing well, thank you!")
    
    elif user_input == "what is your name":
        print(" Chatbot: I am a simple chatbot.")
    
    elif user_input == "bye":
        print(" Chatbot: Goodbye! 👋")
        break
    
    else:
        print(" Chatbot: Sorry, I don't understand.")