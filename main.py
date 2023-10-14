
import pyodbc

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-QRASA28P\SQLEXPRESS;'
                      'Database=KnittingInventory;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Function to add a new yarn item
def add_yarn():
    print("Add a New Yarn Item")
    name = input("Name: ")
    brand = input("Brand: ")
    weight = input("Weight: ")
    color = input("Color: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    # Insert the new yarn item into the database
    cursor.execute("INSERT INTO Yarn (Name, Brand, Weight, Color, Quantity, Price) VALUES (?, ?, ?, ?, ?, ?)",
                   name, brand, weight, color, quantity, price)
    conn.commit()

    print("Yarn item added successfully!")

# Function to add a new needle
def add_needle():
    print("Add a New Needle")
    type = input("Type: ")
    size = input("Size: ")
    material = input("Material: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    # Insert the new needle into the database
    cursor.execute("INSERT INTO Needles (Type, Size, Material, Quantity, Price) VALUES (?, ?, ?, ?, ?)",
                   type, size, material, quantity, price)
    conn.commit()

    print("Needle added successfully!")

# Function to add a new pattern
def add_pattern():
    print("Add a New Pattern")
    name = input("Name: ")
    designer = input("Designer: ")
    difficulty = input("Difficulty: ")
    price = float(input("Price: "))

    # Insert the new pattern into the database
    cursor.execute("INSERT INTO Patterns (Name, Designer, Difficulty, Price) VALUES (?, ?, ?, ?)",
                   name, designer, difficulty, price)
    conn.commit()

    print("Pattern added successfully!")

# Function to add a new project
def add_project():
    print("Add a New Project")
    project_name = input("Project Name: ")
    pattern_id = int(input("Pattern ID: "))
    yarn_id = int(input("Yarn ID: "))
    needle_id = int(input("Needle ID: "))
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")

    # Insert the new project into the database
    cursor.execute("INSERT INTO Projects (ProjectName, PatternID (single integer), YarnID, NeedleID, StartDate, EndDate) "
                   "VALUES (?, ?, ?, ?, ?, ?)", project_name, pattern_id, yarn_id, needle_id, start_date, end_date)
    conn.commit()

    print("Project added successfully!")

while True:
    print("\nKnitting Inventory Management System")
    print("1. Add a Yarn Item")
    print("2. Add a Needle Item")
    print("3. Add a Pattern Item")
    print("4. Add a Project Item")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_yarn()
    elif choice == "2":
        add_needle()
    elif choice == "3":
        add_pattern()
    elif choice == "4":
        add_project()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Close the database connection
conn.close()

