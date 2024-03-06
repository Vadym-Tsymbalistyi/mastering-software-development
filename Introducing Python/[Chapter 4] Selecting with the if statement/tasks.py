# 4.1 Select a number between 1 and 10 and assign it to the variable secret. Select another number between 1 and 10
# and assign it to the guess variable. Next, write conditional checks (if, else and elif) to print the string 'too low'
# if the value of the guess variable is less than 7, 'too high' if it is greater than 7, and 'just right' if it is equal
# to secret.
secret = 9
guess = 9
if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')

# 4.2 Assign True or False values to the variables small and green. Write several if/else statements that will
# display information about whether the following plants match the given conditions: cherry, pea, watermelon, pumpkin.
small = False
green = True
if small:
    if green:
        print('cherry')
    else:
        print('peas')
else:
    if green:
        print('watermelon')
    else:
        print('tikva')
