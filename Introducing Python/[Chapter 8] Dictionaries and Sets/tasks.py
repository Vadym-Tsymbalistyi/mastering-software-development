# 8.1  Create an English-French dictionary called e2f and display it on the screen.
# Here are your first words: dog/chien, cat/chat, and walrus/morse.
e2f = {'dog': 'chien', 'cat': 'chat', 'warlus': 'morse'}
print(e2f)

# 8.2  Using the e2f dictionary, display the French version of the word walrus.
e2f['warlus']
print(e2f['warlus'])

# 8.3  Create a French-English f2e dictionary based on the e2f dictionary. Use the items method.
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
    print(f2e)

# 8.4 Using the f2e dictionary, output the English variant of the word chien.
f2e['chien']
print(f2e['chien'])

# 8.5  Output a set of English words from the keys of the e2f dictionary.
f2e.keys()
print(f2e.keys())

# 8.6 Create a multi-level dictionary of life. Use the following strings for the top-level keys: 'animals', 'plants'
# and 'other'. Make the key 'animals' refer to another dictionary that has the keys 'cats', 'octopi' and 'emus'.
# Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy' and 'Lucy'.
# The other keys should refer to empty dictionaries.
life_list = {'cats': ['Henri', 'Grumpy', 'Lucky'], 'octopi': {}, 'emus': {}}
life = {'animals': life_list, 'plants': {}, 'others': {}}
# 7.7 Print the high-level keys of the life dictionary.
print(life.keys())

# 8.8 Print the keys life['animals'].
print(life['animals'].keys())

# 8.9 Print the values of life['animals']['cats'].
print(life['animals']['cats'])

# 8.10  Use the dictionary generator to create a dictionary of squares. Use range(10) to get the keys.
# Use the squared value of each key as the values.
sqares = {keys: keys * keys for keys in range(10)}
print(sqares)

# 8.11  Use the set generator to create the set odd from the odd numbers of the range(10).
odd = {number for number in range(10) if number % 2 == 1}
print(odd)

# 8.12  Use the inclusion generator to return the string 'Got ' and the numbers from the range(10) range.
# Iterate over this construct using a for loop.
for string in ('Got%s' % namber for namber in range(10)):
    print(string)

# 8.13  Use the zip() function to create a dictionary from a tuple of keys ('optimist', 'pessimist', 'troll')
# and a tuple of values ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').
keys = ('optimist', 'pessimist', 'troll')
valyes = ('The glass is half full', 'The glass is half empru', 'How did you get a glass?')
dict(zip(keys, valyes))
print(dict(zip(keys, valyes)))

# 8.14  Use zip() to create a dictionary named movies that combines the lists titles
# = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] and plots
# = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits'].
titles = ['Creature of Habit', 'Crevel Fate', 'Sharks On a Plane']
phots = ['A nun turns into a monster', 'A haunted yarn shop', 'Chek your exits']
movies = dict(zip(titles, phots))
print(movies)
