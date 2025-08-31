
from datetime import datetime

print("ChatBot: Hello! I'm a basic chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("ChatBot: Hello there! How can I help you?")
    
    elif "your name" in user_input:
        print("ChatBot: I’m RuleBot, your Python chatbot.")
    
    elif "how are you" in user_input:
        print("ChatBot: I'm just code, but I'm functioning perfectly! 😄")
    
    elif "time" in user_input:
        print(f"ChatBot: Current time is {datetime.now().strftime('%H:%M:%S')}")
    
    elif "bye" in user_input:
        print("ChatBot: Bye! Have a nice day! 👋")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")
