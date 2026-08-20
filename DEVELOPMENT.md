# NOELLE Development Log

## Day 1 — Core System & Command Routing

### Completed

- Created the initial NOELLE project
- Set up Git and GitHub repository
- Created `main.py`
- Created `commands.py`
- Implemented a continuous command loop using `while True`
- Added basic commands:
  - `hello`
  - `name`
  - `time`
  - `exit`
- Learned and implemented Python functions
- Learned function parameters
- Learned `return` values
- Learned Python modules and imports
- Separated NOELLE's capabilities into `commands.py`
- Implemented a command dictionary
- Implemented dynamic command routing using function references
- Added unknown-command handling

### Architecture

```text
User Input
    ↓
main.py
    ↓
Command Dictionary
    ↓
Function Reference
    ↓
NOELLE Command
    ↓
Return Response
    ↓
main.py
    ↓
User