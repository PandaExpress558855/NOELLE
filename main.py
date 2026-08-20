import datetime

print("NOELLE is online")

while True:
    command = input("You: ").lower()

    if command == "hello":
        print("NOELLE: Hello!") 

    elif command == "name":
        print("NOELLE: My name is NOELLE.")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"NOELLE: The current time is {current_time}.")

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else: 
        print("NOELLE: I don't understand that yet.")