# IS601_midterm_project

## About
This project processes JSON order data from a dosa restaurant and generates two output files: -
1. customers.json: - Which maps customers phone numbers (formatted as xxx-xxx-xxxx) to customer names.
2. items.json: - A list of ordered items, including their price and total number of times ordered.

## Features
- Reads orders data from JSON file.
- Formats customer phone numbers to xxx-xxx-xxxx.
- Generates customers.json with phone numbers as keys and names as values.
- Generates items.json with items names, prices, and order counts.

## How to run: -
### Step 1: Clone the provided Repository
Commands: -
- git clone https://github.com/ajayaddada/IS601_midterm_project.git 
- cd midterm_project

### Step 2: Run the Python Script
python process_orders.py example_orders.json

### Step 3: View the Output
cat customers.json
cat items.json