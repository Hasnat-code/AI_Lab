class ATM:

    def __init__(self):
        self.balance = 1000

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Deposit successful")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient balance")

    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")


obj = ATM()
obj.menu()