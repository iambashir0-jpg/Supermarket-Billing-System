# ============================================================
#  SmartBuy Supermarket - Billing System
#  Developed by: [Your Name]
#  Date: 2026
#  Description: Automates customer billing, applies discounts,
#               and generates formatted receipts.
# ============================================================

def print_receipt(names, quantities, prices, totals, subtotal, discount, final_amount):
    """Display a formatted receipt for the customer."""
    print("\n")
    print("=" * 50)
    print("       SMARTBUY SUPERMARKET        ")
    print("         Customer Receipt           ")
    print("=" * 50)
    print(f"{'Product':<20} {'Qty':>4} {'Unit Price':>10} {'Total':>10}")
    print("-" * 50)

    for i in range(len(names)):
        print(f"{names[i]:<20} {quantities[i]:>4} {prices[i]:>10.2f} {totals[i]:>10.2f}")

    print("-" * 50)
    print(f"{'Subtotal':<35} Le {subtotal:>10.2f}")

    if discount > 0:
        print(f"{'Discount (10%)':<35} Le {discount:>10.2f}")

    print("=" * 50)
    print(f"{'AMOUNT DUE':<35} Le {final_amount:>10.2f}")
    print("=" * 50)
    print("   Thank you for shopping with us!  ")
    print("=" * 50)
    print()


def get_positive_float(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  [!] Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a number.")


def get_positive_int(prompt):
    """Keep asking until the user enters a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  [!] Please enter a whole number greater than 0.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def process_customer():
    """Handle the full billing workflow for one customer."""

    # --- Arrays (lists) to store product details ---
    names     = []
    quantities = []
    prices    = []
    totals    = []

    subtotal = 0.0

    print("\n" + "-" * 50)
    print("  NEW CUSTOMER")
    print("-" * 50)

    num_products = get_positive_int("  How many products is the customer buying? ")

    # --- Loop to collect each product ---
    for i in range(1, num_products + 1):
        print(f"\n  -- Product {i} --")
        name       = input("  Product Name   : ").strip()
        quantity   = get_positive_int("  Quantity        : ")
        unit_price = get_positive_float("  Price per Unit (Le): ")

        item_total = quantity * unit_price   # Arithmetic operator

        # Store in arrays
        names.append(name)
        quantities.append(quantity)
        prices.append(unit_price)
        totals.append(item_total)

        subtotal += item_total               # Running total

    # --- Decision structure: apply 10% discount if subtotal > Le 500 ---
    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0.0

    final_amount = subtotal - discount

    # --- Display the receipt ---
    print_receipt(names, quantities, prices, totals, subtotal, discount, final_amount)


def main():
    """Main loop — keeps processing customers until cashier exits."""
    print("=" * 50)
    print("   SMARTBUY SUPERMARKET BILLING SYSTEM")
    print("=" * 50)

    # --- Outer loop: continue until cashier chooses to exit ---
    while True:
        print("\n  Options:")
        print("  [1] Process New Customer")
        print("  [2] Exit")
        choice = input("\n  Enter choice (1 or 2): ").strip()

        if choice == "1":
            process_customer()
        elif choice == "2":
            print("\n  Closing system. Goodbye!\n")
            break
        else:
            print("  [!] Invalid choice. Please enter 1 or 2.")


# --- Entry point ---
if __name__ == "__main__":
    main()