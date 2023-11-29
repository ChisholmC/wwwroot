


customers = {}

def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact number: ")

    place_order(name, contact)

    print("Customer added successfully!")

def place_order(customer_name, customer_contact):
    customer_id = len(customers) + 1

    product_name = input(f"Enter product name for {customer_name}: ")
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    total_cost = quantity * unit_price

    order = {
        'order_id': len(customers.get(customer_id, {}).get('orders', [])) + 1,
        'product_name': product_name,
        'quantity': quantity,
        'total_cost': total_cost
    }

    if customer_id not in customers:
        customers[customer_id] = {'name': customer_name, 'contact': customer_contact, 'orders': []}

    customers[customer_id]['orders'].append(order)

    print(f"Order placed for {product_name} (Order ID: {order['order_id']})")

def generate_customer_report(customer_id):
    customer = customers.get(customer_id)

    if customer:
        print(f"Customer Report for {customer['name']}:")
        print(f"Contact: {customer['contact']}")

        total_spending = sum(order['total_cost'] for order in customer['orders'])
        print(f"Total Spending: ${total_spending:.2f}")

        print("Orders:")
        for order in customer['orders']:
            print(f"  Order ID: {order['order_id']}, Product: {order['product_name']}, Quantity: {order['quantity']}, Total Cost: ${order['total_cost']:.2f}")
    else:
        print(f"Customer with ID {customer_id} not found.")

def generate_all_reports():
    for customer_id in customers:
        generate_customer_report(customer_id)
        print("\n" + "=" * 30 + "\n")

def menu():
    while True:
        print("\nOrder and Customer Management System Menu:")
        print("1. Add Customer")
        print("2. Place Order")
        print("3. Generate Customer Report")
        print("4. Generate All Customer Reports")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            place_order(customers.get(customer_id, {}).get('name', 'Unknown'), customers.get(customer_id, {}).get('contact', 'Unknown'))
        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            generate_customer_report(customer_id)
        elif choice == '4':
            generate_all_reports()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()

