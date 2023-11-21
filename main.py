class BankApp:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return 'Transaction successful'
        return 'Invalid deposit amount'

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return 'Transaction successful'
        return 'Zero or insufficient funds'

    def transfer(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount  # Assuming transfer to another account
            return 'Transaction successful'
        return 'Zero or insufficient funds'

    def bundles(self, amount, phonenumber, provider):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return 'Transaction Successful'
        return 'Transaction Unsuccessful'

    def check_balance(self):
        return f'Your available balance is {self.balance}'

# User Interface
def main():
    program = BankApp()
    password = [2345, 4565, 4543, 7865]
    passid = int(input('Enter your password: '))

    if passid in password:
        while True:
            transaction = input('Choose transaction option [deposit, withdrawal, transfer, bundles, check balance, logout]: ').lower()
            if transaction == 'deposit':
                amount = float(input('Enter deposit amount: '))
                print(program.deposit(amount))
            elif transaction == 'withdrawal':
                amount = float(input('Enter withdrawal amount: '))
                print(program.withdraw(amount))
            elif transaction == 'transfer':
                amount = float(input('Enter transfer amount: '))
                print(program.transfer(amount))
            elif transaction == 'bundles':
                amount = float(input('Enter bundles amount: '))
                phonenumber = input('Enter destination phone number: ')
                provider = input('Enter network provider: ')
                print(program.bundles(amount, phonenumber, provider))
            elif transaction == 'check balance':
                print(program.check_balance())
            elif transaction == 'logout':
                print('Goodbye')
                break
            else:
                print('Invalid transaction option')
    else:
        print('Invalid Password')

if __name__ == "__main__":
    main()
