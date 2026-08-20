from commands import say_hello, say_name, tell_time

commands = {
    "hello": say_hello,
    "name": say_name,
    "time": tell_time
}

print("NOELLE is online")

while True:
    command = input("You: ").lower()

    if command in commands:
        response = commands[command]()
        print(response)

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else:
        print("NOELLE: I don't understand that yet.")