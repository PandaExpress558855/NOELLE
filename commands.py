import datetime
import subprocess
import webbrowser

def say_hello():
    return("NOELLE: Hello!")


def say_name():
    return("NOELLE: My name is NOELLE.")


def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"NOELLE: The current time is {current_time}."

def calculate():
    expression = input("NOELLE Calculator: ")

    try:
        parts = expression.split()

        first_number = float(parts[0])
        operator = parts[1]
        second_number = float(parts[2])

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            result = first_number / second_number

        else:
            return "NOELLE: I don't recognize that operator."

        return f"NOELLE: The answer is {result}."

    except:
        return "NOELLE: I couldn't calculate that."

def open_app(app):
    subprocess.Popen(app)
    return f"NOELLE: Opening {app}."


apps = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "browser": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "files": "explorer.exe",
}


def launch_app(app_name):
    if app_name not in apps:
        return f"NOELLE: I don't know how to open {app_name}."

    subprocess.Popen(apps[app_name])
    return f"NOELLE: Opening {app_name}."

websites = {
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "google": "https://www.google.com"
}

def open_website(site):
    if site not in websites:
        return f"NOELLE: I don't know that website."

    webbrowser.open(websites[site])
    return f"NOELLE: Opening {site}."