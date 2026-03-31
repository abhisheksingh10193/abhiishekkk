def print_header():
    border = "=" * 100
    star_line = "*" * 100
    print(border)
    print(star_line)
    print("RAILWAY TICKETS BOOKING SYSTEM".center(100))
    print(star_line)
    print(border)
    print(f"\n{'[ PROJECT DETAILS ]':^100}")
    print(f"{'Name:Abhishek Singh':^100}")
    print(f"{'Registration Number: 25BCE10193':^100}")
    print("\n" + border + "\n")

def register_reservation(records):
    try:
        m = int(input("How many people you want to book tickets for? "))
        for _ in range(m):
            name = input("Enter the name of the passenger: ")
            beginning = input("Enter the boarding station: ")
            destination = input("Enter the destination station: ")

            if beginning.strip().lower() == destination.strip().lower():
                print("Error: Boarding and Destination stations cannot be the same. Registration failed for this passenger.")
                continue

            pnr = int(input("Enter your 10-digit PNR number: "))

            if len(str(pnr)) != 10:
                print("Invalid PNR length. Must be 10 digits. Registration failed for this passenger.")
                continue

            if any(record['pnr'] == pnr for record in records):
                print(f"Error: PNR {pnr} already exists. Registration failed for this passenger.")
                continue

            records.append({
                'name': name,
                'from': beginning,
                'to': destination,
                'pnr': pnr
            })
        print("\nReservation(s) registered successfully!")
    except ValueError:
        print("Invalid input. Please enter numbers where required.")

def update_record(records):
    try:
        pnr_to_find = int(input("Enter your 10-digit PNR number to update: "))
        found = False
        for record in records:
            if record['pnr'] == pnr_to_find:
                found = True
                print("\n1. Update Name\n2. Update Boarding Station\n3. Update Destination")
                choice = input("Choice: ")
                if choice == '1':
                    record['name'] = input("Enter new name: ")
                elif choice == '2':
                    new_from = input("Enter new boarding station: ")
                    if new_from.strip().lower() == record['to'].lower():
                        print("Error: Boarding station cannot be the same as current destination.")
                        return
                    record['from'] = new_from
                elif choice == '3':
                    new_to = input("Enter new destination: ")
                    if new_to.strip().lower() == record['from'].lower():
                        print("Error: Destination cannot be the same as current boarding station.")
                        return
                    record['to'] = new_to
                else:
                    print("Invalid choice.")
                    return
                print("Record updated successfully!")
                break
        if not found:
            print("No reservation found with that PNR.")
    except ValueError:
        print("Invalid PNR format.")

def search_reservation(records):
    try:
        pnr_to_find = int(input("Enter PNR to search: "))
        found = False
        for record in records:
            if record['pnr'] == pnr_to_find:
                print(f"\nName: {record['name']}\nBoarding: {record['from']}\nDestination: {record['to']}")
                found = True
                break
        if not found:
            print("No record found.")
    except ValueError:
        print("Invalid PNR.")

def delete_reservation(records):
    try:
        pnr_to_find = int(input("Enter PNR to delete: "))
        original_count = len(records)
        records[:] = [r for r in records if r['pnr'] != pnr_to_find]
        if len(records) < original_count:
            print("Record deleted successfully.")
        else:
            print("No record found with that PNR.")
    except ValueError:
        print("Invalid PNR.")

def main():
    print_header()
    record_list = []

    while True:
        menu_width = 60
        padding = (100 - menu_width) // 2
        pad_str = " " * padding
        inner_space = menu_width - 2

        print(pad_str + "+" + "-" * inner_space + "+")
        print(pad_str + "|" + " WELCOME TO THE MAIN MENU ".center(inner_space) + "|")
        print(pad_str + "+" + "-" * inner_space + "+")
        print(pad_str + "|" + "  1. Register a Reservation".ljust(inner_space) + "|")
        print(pad_str + "|" + "  2. Update an Existing Record".ljust(inner_space) + "|")
        print(pad_str + "|" + "  3. Search for a Reservation".ljust(inner_space) + "|")
        print(pad_str + "|" + "  4. Delete a Reservation".ljust(inner_space) + "|")
        print(pad_str + "|" + "  5. Exit System".ljust(inner_space) + "|")
        print(pad_str + "+" + "-" * inner_space + "+")

        ans = input("\n" + pad_str + ">>> Choice (1-5): ")

        if ans == '1': register_reservation(record_list)
        elif ans == '2': update_record(record_list)
        elif ans == '3': search_reservation(record_list)
        elif ans == '4': delete_reservation(record_list)
        elif ans == '5': break
        else: print("\n" + pad_str + "[!] Invalid selection.")

        if input("\n" + pad_str + "Return to Menu? (y/n): ").lower() != 'y':
            break

    print("\n" + "="*100)
    print("THANK YOU FOR VISITING - HAVE A NICE DAY".center(100))
    print("="*100)

if __name__ == '__main__':
    main()
