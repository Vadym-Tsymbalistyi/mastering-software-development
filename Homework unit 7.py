#7.1
years_list = [2001,2002,2003,2004,2005,2006]
#7.2
years_list[3]
print(years_list[3])
#7.3
years_list[-1]
print(years_list[-1])
#7.4
things=['mozzarella','cindarella','salmonella']
#7.5
things[1]=things[1].capitalize()
print(things)
#7.6
things[0]=things[0].upper()
print(things)
#7.7
del things[2]
print(things)
#7.8
surcrise=['Grousho','Chico','Harpo']
#7.9
surcrise[-1]=surcrise[-1].lower()
surcrise[-1]=surcrise[-1][::-1]
surcrise[-1].capitalize()
print(surcrise)
#7.10
even=[]
for namber in range(10):
    if namber % 2==0:
        even.append(namber)
print(even)
#7.11
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
start1="".join([text.capitalize() + "!"for text in start1])
for first,second in rhymes:
    print(f"{start1} {first.capitalize()}!")
    print(f"{start2} {second}.")