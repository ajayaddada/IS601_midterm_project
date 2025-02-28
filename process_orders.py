import json
import sys
import re
import os

def format_phone(phone):
    phone = re.sub(r'\D', '', phone)  
    return phone[:3] + "-" + phone[3:6] + "-" + phone[6:] if len(phone) == 10 else phone

def read_orders(filename):
    if not os.path.exists(filename):  
        print(f"Error: {filename} not found.")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            return json.load(file) 
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in", filename)
        sys.exit(1)

def process_orders(orders):
    customers = {}
    items = {}

    for order in orders:
        phone = format_phone(order.get("phone", ""))
        name = order.get("name", "Unknown").strip()

        if phone:
            customers[phone] = name  

        for item in order.get("items", []):
            item_name = item.get("name", "Unknown Item").strip()
            price = item.get("price", 0)

            if item_name in items:
                items[item_name]["orders"] += 1
            else:
                items[item_name] = {"price": price, "orders": 1}

    return customers, items


def write_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    if len(sys.argv) < 2:
        print("Usage: python process_orders.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    orders = read_orders(input_file)
    customers, items = process_orders(orders)

    write_to_file("customers.json", customers)  
    write_to_file("items.json", items)  

    print(" Update completed 'customers.json' and 'items.json'.")


if __name__ == "__main__":
    main()