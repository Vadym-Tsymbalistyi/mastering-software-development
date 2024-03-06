# 5.1 Capitalize the word beginning with the letter m:
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song.replace(" m", " M")
print(song)

# 5.2 Print all the questions from the list and the correct answers in this form:
# Q: question
# A: answer
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
print("Q:", questions[0])
print("A:", answers[1])
print("Q:", questions[1])
print("A:", answers[2])
print("Q:", questions[2])
print("A:", answers[0])

# 5.3 Print the following poem using the old formatting style. Substitute lines such as:
# 'roast beef', 'ham', 'head' and 'clam':
text = '''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.'''
a = ('roast beef', 'ham', 'head', 'clam')
print(text % a)

# 5.4 Write a letter using the new formatting style. Save the proposed string in the variable letter
# (you will need it in the exercise below):
letter = '''
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}
'''

# 5.5 Assign values to the variables 'salutation', 'name', 'product', 'verbed' (past tense verb), 'room', 'animals',
# 'percent', 'spokesman' and 'job_title'. Use the letter.format() function to display the value of the variable letter,
# into which these values are substituted.
print(
    letter.format(salutation='1',
                  name='2',
                  product='3',
                  verbed='4',
                  room='5',
                  animals='6',
                  amount='7',
                  percent='8',
                  spokesman='9',
                  job_title='10')
)

# 5.6 After public polling to choose a name, the following names emerged: English submarine Boaty McBoatface,
# Australian running horse Horsey McHorseface, and Swedish train Trainy McTrainface.
# Use % formatting to display the winning names for Duck, Pumpkin, and Spitz.
name1 = 'Duck'
print("%sy MS%sfase" % (name1, name1))
name2 = 'Gourd'
print("%sy MS%sfase" % (name2, name2))
name3 = 'Spitz'
print("%sy MS%sfase" % (name3, name3))

# 5.7 Do the same using format().
name1 = 'Duck'
text = "{0}y MS{0}fase".format(name1)
print(text)
name2 = 'Gourd'
text = "{0}y MS{0}fase".format(name2)
print(text)
name3 = 'Spitz'
text = "{0}y MS{0}fase".format(name3)
print(text)

# 5.8  And now again using f-string.
name1 = 'Duck'
text = f"{name1}y MS{name1}fase"
print(text)
name2 = 'Gourd'
text = f"{name2}y MS{name2}fase"
print(text)
name3 = 'Spitz'
text = f"{name3}y MS{name3}fase"
print(text)
