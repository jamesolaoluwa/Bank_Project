class bankapp:
    def __init__(self):
        self.balance = 0
        
    def deposit(self):
        amount = float(input('Enter deposit Amount'))
        self.balance += amount
        print('Transaction succesful')
        
    def withdraw(self):
        amount = float(input('Enter Withdrawal Amount'))
        if amount == 0 or amount > self.balance:
            print('Zero or insufficient funds')
        else:
                self.balance -= amount
                print('Transaction succesful')
    def transfer(self):
        amount = input(float('Enter transfer amount: '))
        if amount == 0 or amount > self.balace:
            print('zero or insufficient funds')
        else:
                print('Transaction successful')
    def bundles(self):
        amount = float(input('Enter bundles amount: '))
        if amount == 0 or amount > self.balance:
            print('Transaction Unsuccessful')
        else:
            phonenumber = input('Enter destination phone number: ')
            provider = input('Enter Network Provider: ')
            self.balance -= amount
            print('Transaction Successful')
    def checkbalance(self):
        print(f' Your available balance is {self.balance}')
      
program = bankapp()
password = [2345,4565,4543,7865]
passid = int(input('Enter your password: '))
for x in password:
    if passid == x:
        counter = 0
        operation = input('Enter yes to perform operation: ')
        while operation == 'yes' :
            transaction = input('Choose transaction option [deposit,withdrawal,transfer, bundles, checkbalance,logout]')
            if transaction == 'deposit':
                program.deposit()
            elif transaction == 'withdrawal':
                program.withdrawal()
            elif transaction == 'transfer':
                program.transfer()  
            elif transaction == 'bundles':
                program.bundles()
            elif transaction == 'checkbalance':
                program.checkbalance()
            elif transaction == 'logout':
                print('GOOD BYE')
                break
            operation = input('Enter yes to perform operation')
            counter += 1
else:
    print('Invalid Password')