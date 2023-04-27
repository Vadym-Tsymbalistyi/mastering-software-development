#5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song=song.replace(" m"," M")
print(song)
#5.2
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
print("Q:",questions[0])
print("A:",answers[1])
print("Q:",questions[1])
print("A:",answers[2])
print("Q:",questions[2])
print("A:",answers[0])
#5.3
text='''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.'''
a=('roast beef', 'ham', 'head','clam')
print(text%a)
#5.4
letter='''
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
#5.5
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
#5.6 ,5.7,5.8- I don't understend how to do it :(
name = ["duck", "gourd", "spitz"]
