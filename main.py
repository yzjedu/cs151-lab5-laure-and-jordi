# Programmers: Laure and Jordi
# Course: CS151, Professor Zee
# Due Date: October 17th, 2024
# Lab Assignment: Lab 05
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance, deposit, or withdraw.
# Data In: What action the user would like to take (option), how much user would like to deposit (deposit_amount), How much user would like to withdraw (withdraw_amount)
# Data Out: How much money the user has (balance)
# Credits: None other than class and the read.me file

#Initialize variables
option = ''
balance = 1000
SENTINEL = 'e'

#Ask user which action they would like to make, and error checking
while option != SENTINEL:
    option = input('The purpose of this program is to function as an ATM. Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E.')
    option = option.lower()
    while option != 'd' and option != 'w' and option != 'v' and option!= 'e':
        print('That is an invalid input.')
        option = input('Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E.')
        option = option.lower()

#Code for if user would like to deposit
    if option == 'd':
        deposit_amount = float(input('How much money would you like to deposit?'))
        while deposit_amount < 0:
            print('That is an invalid amount. Please try again.')
            deposit_amount = float(input('How much money would you like to deposit?'))
        balance = deposit_amount + balance

#Code for if user would like to withdraw
    if option == 'w':
        withdraw_amount = float(input('How much money would you like to withdraw?'))
        while withdraw_amount < 0:
            print('That is an invalid amount. Please try again.')
            withdraw_amount = float(input('How much money would you like to withdraw?'))
        if withdraw_amount > balance:
            print('This will make your balance negative, and you will be charged 5% interest')
        balance = balance - withdraw_amount

#Code for if user would like to view balance
    if option == 'v':
        print('Your balance is:', balance)

#Ending code if/when user decides to exit
print('Thank you have a great day!')

