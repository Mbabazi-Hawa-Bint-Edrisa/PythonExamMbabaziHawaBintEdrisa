class WituSacco:
    def __init__(self):
        self.balance = 0
        
    def deposit(self, amount):
        if amount >= 1000:
            self.balance += amount
            print(f"Deposit of {amount} was successful.") 
        else:
            print("Minimum deposit amount is 1000.")   
            
    def withdraw(self, amount):
        if amount >= 500 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} was successful.")
        elif amount > 500:
            print("Minimum withdrawal amount is 500.")
        else:
            print("Insufficient funds.")  
            
    def check_balance(self):
        print(f"Your account balance is: {self.balance}") 

def main():
    sacco = WituSacco()
    print('Welcome to WITU Sacco')
    while True:
        print('\nActivities:')
        print('1. Deposit money')
        print('2. Withdraw money')
        print('3. Check balance')
        print('4. Quit')
        choice = input('Choose activity: ')
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))  
            sacco.withdraw(amount) 
        elif choice == '3': 
            sacco.check_balance()
        elif choice == '4':
            print('Thank you for using WITU Sacco')
            break 
        else:
            print('Your choice is not available. Please choose again.')

if __name__ == '__main__':
    main()

