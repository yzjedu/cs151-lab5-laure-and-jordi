option = ''
balance = 1000
SENTINEL = 'e'
while option != SENTINEL:
    option = input('Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E.')
    option = option.lower()
    while option not in ['d', 'w', 'v','e']:
        print('That is an invalid input.')
        option = input('Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E.')
        option = option.lower()
    if option == 'd':
        deposit_amount = float(input('How much money would you like to deposit?'))
        while deposit_amount < 0:
            print('That is an invalid amount. Please try again.')
            deposit_amount = float(input('How much money would you like to deposit?'))
        balance += deposit_amount
    if option == 'w':
        withdraw_amount = float(input('How much money would you like to withdraw?'))
        while withdraw_amount < 0:
            print('That is an invalid amount. Please try again.')
            withdraw_amount = float(input('How much money would you like to withdraw?'))
        if withdraw_amount > balance:
            print('This will make your balance negative, and you will be charged 5% interest')
        balance -= withdraw_amount
    if option == 'v':
        print('Your balance is:', balance)

print("Thank you have a great day!")


