# NOELLE Development Log

## Day 1 — Core System & Command Routing

### Completed

- Created initial NOELLE project
- Set up Git and GitHub repository
- Created `main.py` and `commands.py`
- Implemented continuous command loop
- Added `hello`, `name`, `time`, and `exit`
- Learned functions, parameters, return values, modules, and imports
- Separated command logic from the main program
- Implemented command dictionary
- Implemented dynamic command routing
- Added unknown-command handling

---

## Day 2 — Calculator & System Automation

### Completed

- Built a calculator command
- Implemented arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Learned string splitting and list indexing
- Learned type conversion with `float()`
- Added basic error handling with `try/except`
- Added Windows application launching using `subprocess`
- Added generic application launcher
- Added support for:
  - Calculator
  - Notepad
- Added website launching using `webbrowser`
- Added support for:
  - Google
  - GitHub
  - YouTube
- Implemented basic command parsing for `open <target>`
- Practiced debugging and resolving import/name errors

### Current Capabilities

NOELLE can currently:

- Respond to basic commands
- Tell its own name
- Tell the current time
- Perform basic calculations
- Open supported Windows applications
- Open supported websites
- Handle unknown commands

### Next

- Refactor command parsing into its own system
- Improve command architecture
- Add more useful system automation
- Begin exploring AI integration