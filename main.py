balance = 1000

while True:
    print(f"\nBalance:${balance}")
    action = input("Type 'w' to withdraw, 'd' to deposit, or 'q' to exit: ").lower()
    
    if action == 'q':
        break
    
    if action in ['w', 'd']:
        amount = float(input("Enter amount:$ "))
        if action == 'w':
            if amount > balance:
                print("You cant take your bank balance to negative duh!")
            else:
                balance -= amount
        elif action == 'd':
            balance += amount
    else:
        print("Invalid command!")