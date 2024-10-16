# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. balance = 1000
2. option = ' '
3. SENTINEL = 'e'
4. As long as the option is not the SENTINEL
   1. Prompt user for input: "Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E."
   2. Convert the input into lowercase 
   3. As long as option is not in ['d','w','v','e']
      1. Output: "That is an invalid input,"
      2. Prompt user for input: "Would you like to deposit, withdraw, view balance, or exit? For deposit, enter D. For withdraw enter W. For view balance enter V, and for exit, enter E."
      3. Convert the input into lowercase
   4. If option equals to 'd'
      1. Prompt user for input: 'How much money would you like to deposit?' (as a float)
      2. As long as the deposit_amount is less than 0
         1. Output: 'That is an invalid amount. Please try again.'
         2. Prompt user for input: 'How much money would you like to deposit?' (as a float)
         3. Calculate new balance by adding the deposited amount to it 
   5. If option equals to 'w'
      1. Prompt user for input: "How much money would you like to withdraw?" (as a float)
      2. As long as the withdraw_amount is less than 0 
         1. Output: 'That is an invalid amount. Please try again.'
         2. Prompt user for input:"How much money would you like to withdraw?" (as a float)
      3. If withdraw_amount is greater than balance
         1. Output: "This will make your balance negative, and you will be charged 5% interest."
         2. Calculate new balance by subtracting the withdraw amount
   6. If option equals to 'v'
      1. Output: "Your balance is:", balance
5. Output: "Thank you have a great day!"