# KnittingInventoryManager

The Knitting Inventory Management System is a Python-based application that allows you to manage your knitting supplies, including yarn, needles, patterns, and knitting projects. This system is designed to help you keep track of your knitting inventory, making it easier to organize your knitting projects and materials.


- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Knitters often accumulate various supplies, including different types of yarn, needles, patterns, and ongoing knitting projects. Keeping track of these supplies manually can be challenging, and that's where the Knitting Inventory Management System comes in. This system allows you to add, update, and view information about your knitting materials, making it easier to plan and execute your knitting projects.

## Features

The Knitting Inventory Management System offers the following features:

Add a New Yarn Item: Record details about the yarn you have, such as name, brand, weight, color, quantity, and price.

Add a New Needle Item: Keep track of your knitting needles by specifying their type, size, material, quantity, and price.

Add a New Pattern Item: Manage your knitting patterns, including their name, designer, difficulty level, and price.

Add a New Project Item: Organize your ongoing knitting projects, specifying project name, associated pattern, yarn, needles, start date, and end date.

User-Friendly Menu: The system provides a user-friendly menu to perform these actions.

Database Integration: Utilizes the SQL Server database for data storage and retrieval.

## Requirements

Before using the Knitting Inventory Management System, make sure you have the following prerequisites:

Python 3.x installed on your system.
The pyodbc library to connect to SQL Server. You can install it using pip install pyodbc.
A SQL Server database set up with the appropriate tables (e.g., Yarn, Needles, Patterns, Projects) to store inventory data. 

## Installation

1. Ensure you have Python 3.x and the pyodbc library installed on your system.
2. Set up a SQL Server database with the required tables. You can create tables using SQL scripts or a database management tool.
3. Update the connection details in the Python script to match your database configuration. Modify the following line with your connection string:

```python
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=YOUR_SERVER_NAME;'
                      'Database=YOUR_DATABASE_NAME;'
                      'Trusted_Connection=yes;')
```

## Usage

To use the Knitting Inventory Management System:

1. Run the Python script (knitting_inventory.py).

2. Follow the menu options to add yarn items, needle items, patterns, and projects.

3. Enter the required details for each item when prompted.

4. Your data will be stored in the SQL Server database.

5. You can exit the system by selecting option 0 in the menu.

Contributing
Contributions to this project are welcome. If you'd like to contribute, feel free to submit pull requests or open issues on the project's repository.

License
This project is licensed under the MIT License. You can find more details in the LICENSE file.
