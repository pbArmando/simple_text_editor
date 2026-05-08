## Text editor
A lightweight text editor built with Python and PySide6 (Qt framework), featuring a terminal-inspired dark theme with green text on black background.

## Overview
This is a simple yet functional text editor designed for users who prefer a clean, terminal-style writing environment. The application provides essential text editing capabilities with a professional dark theme optimized for long writing sessions. Originally developed as part of an academic course (Automatas II - Languages and Automata II), this editor serves as the foundation for future compiler and language processing implementations.

## Features
- **File Management**: Create new files, open existing files, save changes, and save as to new locations
- **Keyboard Shortcuts**: Ctrl+N (new), Ctrl+O (open), Ctrl+S (save), Ctrl+Shift+S (save as), Ctrl+Q (quit)
- **Unsaved Changes Protection**: Prompts user to save before closing if the document has been modified
- **Status Ba**r: Displays current status messages and application information
- **Dark Terminal Theme**: Professional black background with green text for reduced eye strain

## Technologies
- Python 3.8+
- PySide6 (Qt for Python)

## Requirements
- Python 3.8 or higher
- PySide6

## Installation
Clone or download the repository

## Install the required dependency:
- **pip install PySide6**

## Run the application:
- cd "Editor de texto"
- python main.py

## Project Structure
Editor de texto/

├── main.py         # Application entry point

└── mi_ventana.py   # Main window class with all editor functionality

## Future Enhancements
This editor will be extended in future iterations to include:
- **Expression evaluation capabilities**
- **Integration with ANTLR4 for language parsing**
- **Programming language interpreter features**
