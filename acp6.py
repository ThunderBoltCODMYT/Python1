bill_amt = float(input("Enter the bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

due_amount = bill_amt - amount_paid
if due_amount > 0:
    print(f"Due amount: {due_amount}")
else:
    print("No due amount.")