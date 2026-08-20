print("NOELLE is online")

while True:
    command = input("You: ").lower()

    if command == "hello":
        print("NOELLE: Hello!") 

    elif command == "name":
        print("NOELLE: My name is NOELLE.")

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else: 
        print("NOELLE: I don't understand that yet.")