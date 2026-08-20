import datetime


def say_hello():
    return("NOELLE: Hello!")


def say_name():
    return("NOELLE: My name is NOELLE.")


def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"NOELLE: The current time is {current_time}."