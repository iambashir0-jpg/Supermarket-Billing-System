Supermarket Billing System
Project Description
The SmartBuy Supermarket Billing System is a Python-based console application
that automates the customer checkout process for a retail supermarket. It replaces
slow, error-prone manual calculations with a fast, accurate, and user-friendly
billing program.
Features
Accept multiple products per customer (name, quantity, unit price)
Automatically calculates per-item totals and the overall subtotal
Applies a 10% discount when the subtotal exceeds Le 500
Displays a clean, well-formatted receipt
Supports multiple customers in a single session using a loop
Input validation ensures only valid numbers are accepted
How the Program Works
The cashier launches the program.
The cashier selects Option 1 to begin a new customer transaction.
The cashier enters the number of products being purchased.
For each product, the cashier provides:
Product name
Quantity purchased
Price per unit (in Leones)
The system calculates the subtotal.
If the subtotal exceeds Le 500, a 10% discount is automatically applied.
A formatted receipt is printed showing all items, subtotal, discount, and final amount.
The cashier can immediately process the next customer or exit.
How to Run the Program
Requirements
Python 3.x installed on your computer
Steps
Bash
Programming Concepts Used
Concept
Where Used
Variables
subtotal, discount, final_amount, unit_price
Arithmetic Operators
item_total = quantity × unit_price
Decision Structures
if subtotal > 500: apply discount
Loops
while loop for customers; for loop for products
Arrays (Lists)
names[], quantities[], prices[], totals[]
Input / Output
input() and print() throughout
Future Improvements
Save receipts to a text or PDF file
Connect to a product database for barcode scanning
Add a graphical user interface (GUI)
Generate daily sales reports
Support multiple discount tiers
Add user login/authentication for cashiers
How This System Helps Real Businesses
Manual billing in busy supermarkets leads to long queues, human errors, and
unhappy customers. This system solves those issues by:
Eliminating calculation errors – all arithmetic is handled by the computer
Consistent discount application – the 10% rule is always applied correctly
Faster checkout – cashiers enter data quickly and get an instant receipt
Professional receipts – customers receive clear, itemized bills
Scalability – the system can be extended to serve hundreds of customers daily
License
This project is licensed under the MIT License. See LICENSE for details.
