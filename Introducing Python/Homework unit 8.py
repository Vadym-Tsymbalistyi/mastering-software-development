#8.1.
e2f={'dog':'chien','cat':'chat','warlus':'morse'}
print(e2f)
#8.2
e2f['warlus']
print(e2f['warlus'])
#8.3
f2e={}
for english,french in e2f.items():
    f2e[french]=english
    print(f2e)
#8.4
f2e['chien']
print(f2e['chien'])
#8.5
f2e.keys()
print(f2e.keys())
#8.6
life_list = { 'cats':['Henri','Grumpy','Lucky'],'octopi':{},'emus':{}}
life = {'animals':life_list,'plants':{},'others':{}}
print(life.keys())
#8.7
print(life['animals'].keys())
#8.9
print(life['animals']['cats'])
#8.10
sqares ={keys : keys * keys for keys in range(10)}
print(sqares)
#8.11
odd={number for number in range(10) if number %2==1}
print(odd)
#8.12
for string in ('Got%s'  % namber for namber in range(10)):
    print(string)
#8.13
keys =('optimist','pessimist','troll')
valyes = ('The glass is half full','The glass is half empru','How did you get a glass?')
dict(zip(keys,valyes))
print(dict(zip(keys,valyes)))
#8.14
titles=['Creature of Habit','Crevel Fate','Sharks On a Plane']
phots=['A nun turns into a monster','A haunted yarn shop','Chek your exits']
movies=dict(zip(titles,phots))
print(movies)