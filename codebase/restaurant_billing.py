# Restaurant Billing System
# PS No. 45 | Python 3

import os

DISCOUNT_RATE = 0.10
GST_RATE = 0.05
DISCOUNT_LIMIT = 500


def load_menu(filename="menu.txt"):
    """Load menu items and prices from menu.txt into a dictionary."""
    menu = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and "," in line:
                    item, price = line.split(",", 1)
                    menu[item.strip().title()] = int(price.strip())

    # Fallback menu in case menu.txt is missing or empty
    if not menu:
        menu = {
            "Dosa": 80,
            "Idli": 40,
            "Thali": 150,
            "Tea": 20
        }
    return menu


def display_menu(menu):
    print("\n========== RESTAURANT MENU ==========")
    for item, price in menu.items():
        print(f"{item:<15} Rs. {price}")
    print("=====================================")


def get_quantity():
    while True:
        value = input("Quantity: ").strip()
        try:
            quantity = int(value)
            if quantity < 1:
                print("Quantity must be at least 1.")
            else:
                return quantity
        except ValueError:
            print("Invalid quantity. Enter a whole number.")


def take_order(menu):
    """Take multiple items using a loop and store ordered items in a list."""
    ordered_items = []
    available_str = ", ".join(menu.keys())

    while True:
        raw_input = input("Order item (or 'Generate bill'): ").strip()

        if raw_input.lower() in ("generate bill", "bill", "done"):
            if ordered_items:
                break
            print("Please add at least one item before generating the bill.")
            continue

        item = raw_input.title()
        if item not in menu:
            print(f"Item not on the menu. Available: {available_str}")
            continue

        quantity = get_quantity()
        price = menu[item]
        amount = price * quantity

        # Update existing item entry in the list or append a new record
        found = False
        for entry in ordered_items:
            if entry["item"] == item:
                entry["quantity"] += quantity
                entry["amount"] += amount
                found = True
                break

        if not found:
            ordered_items.append({
                "item": item,
                "price": price,
                "quantity": quantity,
                "amount": amount
            })

        print(f"{item} x{quantity} added | Amount: {amount}")

    return ordered_items


def calculate_subtotal(ordered_items):
    return sum(entry["amount"] for entry in ordered_items)


def calculate_discount(subtotal):
    return subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_LIMIT else 0.0


def calculate_gst(amount_after_discount):
    return amount_after_discount * GST_RATE


def calculate_total(subtotal, discount, gst):
    return (subtotal - discount) + gst


def print_bill(ordered_items):
    subtotal = calculate_subtotal(ordered_items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    gst = calculate_gst(discounted_amount)
    grand_total = calculate_total(subtotal, discount, gst)

    print("\n" + "=" * 46)
    print("               RESTAURANT BILL")
    print("=" * 46)
    for entry in ordered_items:
        print(f"{entry['item']:<12} x{entry['quantity']:<4} = {entry['amount']}")

    print("-" * 46)
    if discount > 0:
        print(f"Subtotal: {subtotal} | Discount (10%): {discount:.2f}")
    else:
        print(f"Subtotal: {subtotal} | Discount: {discount:.2f}")
    print(f"GST (5%): {gst:.2f} | Grand Total: {grand_total:.2f}")
    print("=" * 46)
    print("          Thank you! Visit again.")
    print("=" * 46)


def main():
    menu = load_menu("menu.txt")
    print("Welcome to the Restaurant Billing System!")
    display_menu(menu)
    ordered_items = take_order(menu)
    print_bill(ordered_items)


if __name__ == "__main__":
    main()
