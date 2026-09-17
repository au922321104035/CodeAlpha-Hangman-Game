# File Organizer

## About the Project

This is a simple File Organizer automation project developed using Python.

The program checks a folder and moves `.jpg` files into a separate `JPG_Files` folder automatically.

## Features

- Checks files in a folder
- Identifies `.jpg` files
- Creates a `JPG_Files` folder automatically
- Moves JPG files into the folder
- Uses Python automation

## Technologies Used

- Python
- os
- shutil

## How It Works

The program checks the `Test_Files` folder for JPG files.
If the `JPG_Files` folder does not exist, it creates it automatically.
Then it moves all JPG files into the `JPG_Files` folder.

## How to Run

Run the following command in the terminal:

```bash
python file_organizer.py
