import datetime

def say_hello():
    print("NOELLE: Hello!")


def say_name():
    print("NOELLE: My name is NOELLE.")


def greet(name):
    print(f"NOELLE: Hello, {name}!")

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"NOELLE: The current time is {current_time}.")