total_sales = 0
net_sales = 0
num_sales = 0
total_expenses = 0

while True:
    entered_amt = input("Enter an amount (or press Enter to exit):")
    
    if entered_amt == '':
        break  # Exit the loop if the user presses Enter

    num_sales += 1

    try:
        entered_amt = float(entered_amt)
        net_sales += entered_amt
        print("Net sales:", net_sales)
        if entered_amt > 0:
            total_sales += entered_amt
        else:
            total_expenses += entered_amt

    except ValueError:
        print("Enter a valid amount!")

print("Number of sales:", num_sales)
print("Total sales:", total_sales)
print("Total expenses:", total_expenses)
print(f"Net sales: {net_sales}")
