# Python File Tools

A collection of Python scripts for file organization and search automation.

This project contains simple command-line tools built with Python's standard library to automate everyday file management tasks.

## Features

### File Organizer

- Organizes files by extension.
- Moves PDF files into the `PDF` folder.
- Moves DOCX files into the `documents` folder.
- Moves ZIP files into the `ARCHIVE` folder.
- Skips unsupported file types.
- Detects filename conflicts to prevent overwriting existing files.
- Handles file operation errors.
- Displays a summary of completed operations.

### File Search

- Searches for files by full or partial filename.
- Filters results by file extension.
- Searches recursively through nested directories.
- Supports case-insensitive matching.
- Displays matching filenames and the total number of results.
- Saves search results to a `result.txt` report.

## Requirements

- Python 3.10 or later
- No third-party packages required

## Project Structure

```text
python-file-tools/
├── README.md
├── file_organizer.py
├── file_search.py
└── .gitignore
```

## Setup

1. Clone or download this repository.
2. Open the project in your preferred Python IDE.
3. Update the `folder` variable in the script to specify the directory you want to use.

Example:

```python
folder = Path(r"C:\Users\YourName\Downloads")
```

Replace the example path with your actual directory path.

## Usage

Run the file organizer:

```bash
python file_organizer.py
```

Run the file search tool:

```bash
python file_search.py
```

For file search, enter a filename or part of a filename and the desired extension, such as `pdf`, `.pdf`, or `docx`.

