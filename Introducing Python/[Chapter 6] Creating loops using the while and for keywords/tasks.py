# 6.1 Use the for loop to display the values of the list [3, 2, 1, 0].
start = [3, 2, 1, 0]
for leter in start:
    print(leter)

# 6.2 Assign a value of 7 to the guess_me variable and a value of 1 to the number variable.
# Write a while loop that compares the variables number and guess_me.
# Print the 'too low' line if the value of the start variable is less than the value of the guess_me variable.
# If the value of the number variable is equal to the value of the guess_me variable, print the 'found it!' line
# and exit the loop. If the value of the number variable is greater than the value of the guess_me variable,
# print the 'oops' line and exit the loop. Increase the value of the number variable at the loop exit.
guess_me = 7
namber = 1
while True:
    if namber < guess_me:
        print('too lov')
    elif namber == guess_me:
        print('found it!')
        break
    elif namber > guess_me:
        print('oops')
        break
    namber += 1

# 6.3 Assign the value 5 to the guess_me variable. Use the for loop to loop through the range(10) variable number.
# If the value of the number variable is less than the value of guess_me, display the message 'too low'.
# If it is equal to the guess_me value, print the 'found it!' message and then exit the loop.
# If the value of the number variable is greater than guess_me, print the 'oops' message and exit the loop.
guess_me = 5
for namber in range(10):
    if namber < guess_me:
        print('too lov')
    elif namber == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
