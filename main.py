from commands import say_hello, say_name, greet, tell_time

print("NOELLE is online")

while True:
    command = input("You: ").lower()

    if command == "hello":
        name = input("What is your name? ")
        greet(name)

    elif command == "name":
        say_name()

    elif command == "time":
        tell_time()

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else:
        print("NOELLE: I don't understand that yet.")