# smart-todo-app-
A command-line todo application with advanced features powered by regular expressions for intelligent task parsing and management.

The features included are:
-Task management feature to handle the task CRUD.
-Smart task parsing with regex to parse and extract components.
-Search and filter with regex 
-Task Validation to handle formats

Installation instructions
-created the project directory
-initialized git with git init
-initialized poetry to handle project structure and dependencies such as, dateutil and pytest
-Activated the virtual environment with poetry shell

Testing Instructions
-To test app run python src/main.py
-Choose from the available options such as add, delete,list search and filter , etc.
Example usage 
# Add tasks with smart parsing
>add "Go to the bathroom @home #high due:2025-1-20 assigned:martins@example.com"
# Output
Task added: Go to the bathroom
Tags: home | Due: 2025-1-20 | Priority: None
