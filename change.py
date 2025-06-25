# Owen Fissel
# xx-owen-xx
# 06/24/25
# prompt user to enter an intiger between 0-99, outpout the fewest number of coins that would get you that monitary value (input)

# calls for input to be an integer and breaks down the input to be its own line.
cents = int(input('Please enter an amount of cents less than a dollar.\n'))

# divides our how many times 25 will go into our input
quarters =  cents // 25
# the % gives our reminder for all of the coins
cents = cents % 25

# divides our new total 10 will go into our new total
dimes = cents //10
cents = cents % 10

# divides our new total divided by 5
nickels = cents // 5
cents = cents % 5

pennies = cents // 1
cents = cents % 1

print('Your change will be:')
print('Q:', quarters)
print('D:', dimes)
print('N:', nickels)
print('P:', pennies)
