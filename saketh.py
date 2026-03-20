print("AI Bot Started (type 'exit' to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Bye! See you tomorrow.")
        break

    elif "ece" in user.lower():
        print("Bot: I can help with electronics & coding.")

    elif "gym" in user.lower():
        print("Bot: Push–Pull–Legs is a good split.")

    elif "study" in user.lower():
        print("Bot: Study 50 min, break 10 min.")

    else:
        print("Bot: I am learning. Ask about ECE, Gym, or Study.")
