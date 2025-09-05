# Daily-DiaryDaily Diary App (Python)

This is a simple Python program that allows you to write and read personal diary entries. Each diary entry is saved with the current date as its filename.

FEATURES

Create a new diary entry (saved in a file named YYYY-MM-DD.txt).

Append multiple entries to the same date file.

Store created diary dates in a file named created.txt.

Read any past diary by entering the date.

Simple and user-friendly menu.

REQUIREMENTS

Python 3.10 or above (because the program uses match-case syntax).

Works on Windows, Linux, and macOS.

HOW TO RUN

Save the code in a file named diary.py.

Open the terminal or command prompt in the same folder.

Run the program using:
python diary.py

USAGE

When the program runs, you will see a menu:

1 - Create Diary Entry
2 - Read Diary
3 - Exit

Option 1: Create a diary entry

Type your text and press Enter.

The entry will be saved in a file named with today’s date (e.g., 2025-09-05.txt).

Option 2: Read a diary

Enter a date in the format YYYY-MM-DD.

If a diary file exists for that date, it will be displayed.

Option 3: Exit the program.

EXAMPLE

Creating an entry:
Write your diary entry: Had a great day learning Python!
Diary entry saved successfully!

Reading an entry:
Enter the date (YYYY-MM-DD) of the diary you want to read: 2025-09-05

--- Diary Entry ---
Had a great day learning Python!
NOTES

All entries for the same date are saved in the same file.

Each new entry is stored on a new line.

The created.txt file contains the list of dates for which diaries exist.

FUTURE IMPROVEMENTS

Add password protection.

Add keyword search in diary entries.

Create a graphical user interface (GUI).

Export diaries to PDF or Word.
