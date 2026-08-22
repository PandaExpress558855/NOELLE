from commands import (
    say_hello,
    say_name,
    tell_time,
    calculate,
    launch_app,
    open_website,
    apps,
    websites,
)

commands = {
    "hello": say_hello,
    "name": say_name,
    "time": tell_time,
    "calculator": calculate,
}

print("NOELLE is online")

while True:
    command = input("You: ").lower()
    parts = command.split()

    if len(parts) == 2 and parts[0] == "open":
        target = parts[1]

        if target in apps:
            response = launch_app(target)

        elif target in websites:
            response = open_website(target)

        else:
            response = f"NOELLE: I don't know how to open {target}."

        print(response)

    if command in commands:
        response = commands[command]()
        print(response)

    elif command == "exit":
        print("NOELLE: Goodbye!")
        break

    else:
        print("NOELLE: I don't understand that yet.")