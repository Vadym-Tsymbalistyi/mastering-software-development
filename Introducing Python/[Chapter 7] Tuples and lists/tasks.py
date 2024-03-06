# 7.1 Create a years_list containing the year you were born and each subsequent year until your fifth birthday.
# For example, if you were born in 1980, the list would look like this: years_list = [1980, 1981, 1982, 1983, 1984, 1985].
years_list = [2001, 2002, 2003, 2004, 2005, 2006]

# 7.2  Which year on the years_list was your third birthday? Keep in mind, in the first year you were 0 years old.
years_list[3]
print(years_list[3])

# 7.3 In which year from years_list were you the most years old?
years_list[-1]
print(years_list[-1])

# 7.4  Create a list of things containing three items: "mozzarella", "cinderella", "salmonella".
things = ['mozzarella', 'cindarella', 'salmonella']

# 7.5 Capitalize the item in the list of things that means person, and then print the list. Did the item in the list change?
things[1] = things[1].capitalize()
print(things)

# 7.6 Capitalize the cheesy element of the list of things and then print the list.
things[0] = things[0].upper()
print(things)

# 7.7 Remove a disease from the list of things, get the Nobel Prize, and then display the list.
del things[2]
print(things)

# 7.8  Create a list with the items "Groucho," "Chico," and "Harpo"; name it surprise.
surcrise = ['Grousho', 'Chico', 'Harpo']

# 7.9 Write the last element of the list surprise with a lowercase letter,
# then print that line in reverse order and with an uppercase letter.
surcrise[-1] = surcrise[-1].lower()
surcrise[-1] = surcrise[-1][::-1]
surcrise[-1].capitalize()
print(surcrise)

# 7.10  Use list inclusion to create a list named even that contains even numbers in the range(10).
even = []
for namber in range(10):
    if namber % 2 == 0:
        even.append(namber)
print(even)

# 7.11  Try to create a jump rope rhyme generator. Type a sequence of two-line rhymes.
# Start the program with this fragment:
# start1 = ["fee", "fie", "foe"]
# rhymes = [
# ("flop", "get a mop"),
# ("fope", "turn the rope"),
# ("fa", "get your ma"),
# ("fudge", "call the judge"),
# ("fat", "pet the cat"),
# ("fog", "walk the dog"),
# ("fun", "say we're done"),
# ]
# start2 = "Someone better"
# Then follow the instructions.
# For each tuple (first, second) in the rhymes list.
# For the first string:
# - display each line of the start1 list: start it with a capital letter and end it with an exclamation point with a space;
# - display the value of the variable first, also capitalizing it and ending with an exclamation point.
# For the second line:
# - print the value of the start2 variable and a space;
# - display the value of the second variable and a dot.
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
start1 = "".join([text.capitalize() + "!" for text in start1])
for first, second in rhymes:
    print(f"{start1} {first.capitalize()}!")
    print(f"{start2} {second}.")
