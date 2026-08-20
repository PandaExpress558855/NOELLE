import datetime

def greet(name):
    print(f"NOELLE: Hello, {name}!")

def say_name():
    print("NOELLE: My name is NOELLE.")

print("NOELLE is online")

while True:
    command = input("You: ").lower()

    if command == "hello":
        name = input("What is your name? ")
        greet(name)

    elif command == "name":
        say_name()

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"NOELLE: The current time is {current_time}.")

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else:
        print("NOELLE: I don't understand that yet.")