import datetime

# Get today's date as filename
today = str(datetime.date.today())

# Function for creating new diary entry
def create_diary():
    with open(f"{today}.txt", "a") as f:  # append instead of overwrite
        entry = input("Write your diary entry: ")
        f.write(entry + "\n")  # add newline after each entry
    
    with open("created.txt", "a") as c:
        c.write(today + "\n")  # store date with newline
    
    print("Diary entry saved successfully!")

# Function for reading previous diaries
def read_diary():
    date = input("Enter the date (YYYY-MM-DD) of the diary you want to read: ")
    try:
        with open(f"{date}.txt", "r") as f:
            print("\n--- Diary Entry ---")
            print(f.read())
            print("-------------------\n")
    except FileNotFoundError:
        print("Diary for this date was not found!")

# Main program loop
while True:
    print("\nHi User! What do you want to do today?")
    print("1 - Create Diary Entry")
    print("2 - Read Diary")
    print("3 - Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                create_diary()
            case 2:
                read_diary()
            case 3:
                print("Goodbye! 👋")
                break
            case _:
                print("Invalid option! Please try again.")
    except ValueError:
        print("Please enter a valid number.")
            