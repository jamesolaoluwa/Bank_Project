# BankApp

A simple Python console-based banking application that allows users to perform basic banking operations like deposit, withdrawal, transfer, checking balance, and more.

## Features

- **Deposit:** Users can deposit funds into their account.
- **Withdrawal:** Users can withdraw funds from their account, with checks for insufficient funds.
- **Transfer:** Users can transfer funds to another account.
- **Bundles:** Users can purchase mobile bundles, specifying the destination phone number and network provider.
- **Check Balance:** Users can check their account balance.
- **Security:** The application requires a password to access, ensuring user privacy.

## How to Use

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/BankApp.git
```

2. Run the `bank_app.py` file in your Python environment.

```bash
python bank_app.py
```

3. Enter the password (e.g., 2345, 4565, 4543, or 7865) to access the banking application.

4. Choose your desired transaction (deposit, withdrawal, transfer, bundles, check balance, or logout) and follow the prompts.

5. Perform transactions as needed.

## Example Usage

```python
# Create a bankapp object
program = bankapp()

# Enter the password to access the application
passid = int(input('Enter your password: '))

# Check if the password is valid
for x in password:
    if passid == x:
        counter = 0
        operation = input('Enter yes to perform operation: ')
        while operation == 'yes':
            transaction = input('Choose transaction option [deposit, withdrawal, transfer, bundles, check balance, logout]')
            if transaction == 'deposit':
                program.deposit()
            elif transaction == 'withdrawal':
                program.withdrawal()
            elif transaction == 'transfer':
                program.transfer()
            elif transaction == 'bundles':
                program.bundles()
            elif transaction == 'check balance':
                program.checkbalance()
            elif transaction == 'logout':
                print('GOOD BYE')
                break
            operation = input('Enter yes to perform operation')
            counter += 1
else:
    print('Invalid Password')
```
