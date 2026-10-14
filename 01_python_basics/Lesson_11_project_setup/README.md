

# Task Due-Date Automation

A small Python project that demonstrates a clean project structure,
virtual environments, dependency management, and Git readiness.

## Features

- Organized `src` package structure
- Virtual environment support
- Dependency management with `requirements.txt`
- Git-ready project setup

## Requirements

- Python 3.10 or newer
- Git

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the project:

```powershell
python main.py
```

## Project structure

```text
Lesson_11_project_setup/
├── src/
│   ├── __init__.py
│   └── app.py
├── data/
│   └── tasks.csv
├── output/
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

## What I learned

- How to isolate project dependencies with `venv`.
- How to install and record dependencies.
- How to prepare a Python project for Git and GitHub.