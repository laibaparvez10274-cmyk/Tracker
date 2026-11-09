print("=== Laiba ka Expense Tracker ===")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. view all Expense")
    print("3. Total ")
    print("4. Exit")

    choice = input("choose one (1-4): ")

    if choice == "1":
        item = input("spend on wht? ")
        amount = int(input("how much rupees? "))
        expenses.append((item, amount))

    
        with open("expenses.txt", "a") as file:
            file.write(f"{item} - {amount} Rs\n")
        print("Save ho gaya!")

    elif choice == "2":
        print("\n--- Your expenses ---")
        if len(expenses) == 0:
            print("No Expense right now.")
        else:
            for item, amount in expenses:
                print(f"{item} : {amount} Rs")

    elif choice == "3":
        total = 0
        for item, amount in expenses:
            total = total + amount
        print(f"\nTotal Expense: {total} Rs")

    elif choice == "4":
        print("Allah Hafiz! Expense Tracker is going off.")
        break

    else:
        print("wrong option, try again!")