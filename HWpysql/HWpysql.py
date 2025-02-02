import sqlite3


conn = sqlite3.connect('HWpysql.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def execute_modify_query(_cursor, _conn, query) -> None:
    """Execute a modify query (insert, update, delete)"""
    _cursor.execute(query)
    _conn.commit()

def execute_read_query(_cursor, query) -> list:
    """Execute a read query (select)"""
    _cursor.execute(query)
    _rows = _cursor.fetchall()
    _answer = []
    for _row in _rows:
        _answer.append(dict(_row))
    return _answer

def print_color(message, color="red"):
    """Print a string with color"""
    match color:
        case "red":
            COLOR = '\033[31m'
            RESET = '\033[0m'
        case "blue":
            COLOR = '\033[34m'
            RESET = '\033[0m'
        case _:
            COLOR = '\033[31m'
            RESET = '\033[0m'
    print(f"{COLOR}{message}{RESET}")


def add_vehicle():
    """Adds a new vehicle to the garage"""
    car_number = input("Enter vehicle license plate: ")
    car_problem = input("Enter the car's problem: ")
    owner_ph = input("Enter owner's phone number: ")
    try:
        execute_modify_query(cursor, conn, f"""
            INSERT INTO garage (car_number, car_problem, owner_ph)
            VALUES ('{car_number}', '{car_problem}', '{owner_ph}')
        """)
        print_color("Vehicle added successfully!", "blue")
    except Exception as e:
        print_color(f"Error: {e}", "red")

def mark_repair_completed():
    """Marks a vehicle's repair as completed"""
    car_number = input("Enter vehicle license plate: ")
    vehicle = execute_read_query(cursor, f"SELECT * FROM garage WHERE car_number='{car_number}'")
    if not vehicle:
        print_color("Vehicle not found in the garage!", "red")
    elif vehicle[0]['fixed'] == 1:
        print_color("Repair already completed!", "red")
    else:
        execute_modify_query(cursor, conn, f"UPDATE garage SET fixed=1 WHERE car_number='{car_number}'")
        print_color("Repair marked as completed.", "blue")

def remove_vehicle():
    """Removes a vehicle from the garage after repair completion"""
    car_number = input("Enter vehicle license plate: ")
    vehicle = execute_read_query(cursor, f"SELECT * FROM garage WHERE car_number='{car_number}'")
    if not vehicle:
        print_color("Vehicle not found in the garage!", "red")
    elif vehicle[0]['fixed'] == 0:
        print_color("Repair not completed! Cannot remove vehicle.", "red")
    else:
        print_color(f"Call owner at {vehicle[0]['owner_ph']} to inform about pickup.", "green")
        execute_modify_query(cursor, conn, f"DELETE FROM garage WHERE car_number='{car_number}'")
        print_color("Vehicle removed from garage.", "blue")

def show_vehicles_under_repair():
    """Displays the number of vehicles under repair"""
    vehicles = execute_read_query(cursor, "SELECT COUNT(*) AS count FROM garage WHERE fixed=0")
    print_color(f"Currently {vehicles[0]['count']} vehicles are under repair.", "blue")

while True:
    print()
    print("1. Add a new vehicle for repair")
    print("2. Mark repair as completed")
    print("3. Remove vehicle from garage")
    print("4. Show vehicles currently under repair")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_vehicle()
    elif choice == "2":
        mark_repair_completed()
    elif choice == "3":
        remove_vehicle()
    elif choice == "4":
        show_vehicles_under_repair()
    elif choice == "5":
        break
    else:
        print_color("Invalid option, try again.", "red")

conn.close()