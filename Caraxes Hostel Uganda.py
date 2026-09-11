import json

hostel_fee = 800000

hostels = {
    "block A": {
        "rooms": {
            "A101": {"capacity": 4, "occupants": []},
            "A102": {"capacity": 4, "occupants": []},
            "A103": {"capacity": 4, "occupants": []}
        }
    },

    "block B": {
        "rooms": {
            "B101": {"capacity": 4, "occupants": []},
            "B102": {"capacity": 4, "occupants": []},
            "B103": {"capacity": 4, "occupants": []}
        }
    },

    "block C": {
        "rooms": {
            "C101": {"capacity": 4, "occupants": []},
            "C102": {"capacity": 4, "occupants": []},
            "C103": {"capacity": 4, "occupants": []}
        }
    }
}
def display_hostels():
    print("\n===== HOSTEL ROOMS =====")

    for block, data in hostels.items():
        print("\n" + block.upper())

        for room, details in data["rooms"].items():
            capacity = details["capacity"]
            occupants = details["occupants"]

            print(room, "-", len(occupants), "/", capacity, "occupied")

            if len(occupants) > 0:
                for student in occupants:
                    print("  Name:", student["name"], "| Age:", student["age"])
        


def student_exists(name):
    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:
                if student["name"].lower() == name.lower():
                    return True

    return False

def find_room(room_number):
    for block, data in hostels.items():
        if room_number in data["rooms"]:
            return data["rooms"][room_number]

    return None

def add_student():
    print("\nADD STUDENT")

    name = input("Enter student name: ")

    if not name.replace(" ", "").isalpha():
        print("Please enter a valid name using letters only.")
        return
    
    registration_number = input("Enter registration number:")

    if registration_number == "":
        print("registration number cannot be empty.")
        return
    
    if student_exists(name):
        print("Student already exists.")
        return

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Please enter a valid age.")
        return
    if age <= 0:
        print("age must be greater than 0.")
        return

    room_number = input("Enter room number: ")

    room = find_room(room_number)

    if room is None:
        print("Room not found.")
        return

    if len(room["occupants"]) >= room["capacity"]:
        print("Room is full.")
        return

    try:
        fees = hostel_fee
        paid = float(input("Enter amount paid: "))
    except ValueError:
        print("Please enter valid amounts.")
        return

    if fees < 0 or paid < 0:
        print("Fees and payment cannot be negative.")
        return

    if paid > fees:
        print("Amount paid cannot be greater than the total fees.")
        return

    room["occupants"].append({
        "name": name,
        "age": age,
        "registration_number":registration_number,
        "fees": fees,
        "payments": [paid]
    })

    print(name, "has been added to", room_number)


def remove_student():
    print("\n===== REMOVE STUDENT =====")

    name = input("Enter student name: ")

    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:
                if student["name"].lower() == name.lower():
                    details["occupants"].remove(student)
                    print(name, "has been removed from", room)
                    return

    print("Student not found.")


def search_student():
    print("\nSEARCH STUDENT")
    print("1. Search by name")
    print("2. Search by registration number")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_value = input("Enter student name: ").strip()

    elif choice == "2":
        search_value = input("Enter registration number: ").strip()

    else:
        print("Invalid choice.")
        return

    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:

                if choice == "1":
                    found = student["name"].lower() == search_value.lower()
                else:
                    found = student["registration_number"].lower() == search_value.lower()

                if found:
                    print("\nStudent found!")
                    print("Name:", student["name"])
                    print("Registration number:", student["registration_number"])
                    print("Age:", student["age"])
                    print("Block:", block)
                    print("Room:", room)
                    return
 
    print("Student not found.")
    
def show_occupancy():
    print("\nHOSTEL OCCUPANCY")

    for block, data in hostels.items():
        total_spaces = 0
        occupied_spaces = 0

        print("\n" + block.upper())

        for room, details in data["rooms"].items():
            capacity = details["capacity"]
            occupied = len(details["occupants"])

            total_spaces += capacity
            occupied_spaces += occupied

            print(room, ":", occupied, "/", capacity, "occupied")

        print(
            "block total:",
            occupied_spaces,
            "/",
            total_spaces,
            "occupied"
        )

def show_fees():
    print("\nSTUDENT FEES")
    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:

                total_paid = sum(student["payments"])
                balance = student["fees"] - total_paid

                print("\nName:", student["name"])
                print("Registration number:", student["registration_number"])
                print("Room:", room)
                print("Total fees:", student["fees"])
                print("Payments:", student["payments"])
                print("Total paid:", total_paid)
                print("Balance:", balance)
def record_payment():
    print("\nRECORD FEE PAYMENT")

    registration_number = input("Enter student registration number: ").strip()

    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:

                if student["registration_number"].lower() == registration_number.lower():

                    total_paid = sum(student["payments"])
                    balance = student["fees"] - total_paid

                    print("Student:", student["name"])
                    print("Current balance:", balance)

                    if balance <= 0:
                        print("Fees are already fully paid.")
                        return

                    try:
                        amount = float(input("Enter payment amount: "))
                    except ValueError:
                        print("Please enter a valid amount.")
                        return

                    if amount <= 0:
                        print("Payment must be greater than 0.")
                        return

                    if amount > balance:
                        print("Payment cannot be greater than the outstanding balance.")
                        return

                    student["payments"].append(amount)

                    new_balance = student["fees"] - sum(student["payments"])

                    print("Payment recorded successfully.")
                    print("New balance:", new_balance)
                    return

    print("Student not found.")
    
def show_defaulters():
    print("\nFEE DEFAULTERS")

    try:
        threshold = float(input("Enter balance threshold: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if threshold < 0:
        print("Threshold cannot be negative.")
        return

    found = False

    for block, data in hostels.items():
        for room, details in data["rooms"].items():
            for student in details["occupants"]:

                total_paid = sum(student["payments"])
                balance = student["fees"] - total_paid

                if balance > threshold:
                    found = True

                    print("\nName:", student["name"])
                    print("Registration number:", student["registration_number"])
                    print("Room:", room)
                    print("Outstanding balance:", balance)

    if not found:
        print("No fee defaulters found.")
        
def save_data():
    try:
        
        with open("hostel_data.json", "w") as file: 
           json.dump(hostels, file, indent=4)

        print("Hostel data saved successfully.")

    except OSError:
        print("unable to save hostel data.")

def load_data():
    global hostels

    try:
        with open("hostel_data.json", "r") as file:
            hostels = json.load(file)

    except FileNotFoundError:
        print("No saved hostel data found. Starting with empty hostels.")

    except json.JSONDecodeError:
        print("Saved hostel data is damaged. Starting with empty hostels.")     
        
               
def main():
    load_data()
    show_occupancy()
    
    while True:
        print("\nCARAXES HOSTEL UGANDA")
        print("1. Display hostels")
        print("2. Add student")
        print("3. Remove student")
        print("4. Search student")
        print("5. Show occupancy")
        print("6. Show fees")
        print("7. Record payment")
        print("8. Show fee defaulters")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_hostels()

        elif choice == "2":
            add_student()

        elif choice == "3":
            remove_student()

        elif choice == "4":
            search_student()

        elif choice == "5":
            show_occupancy()

        elif choice == "6":
            show_fees()

        elif choice == "7":
            record_payment()

        elif choice == "8":
            show_defaulters()

        elif choice == "9":
            save_data()
            print("Exiting hostel management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
