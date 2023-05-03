count = 1
while count <= 5:
    print(count)
    count+=1
word='thud'
for leter in word:
    print(leter)
#6.1
start = [3,2,1,0]
for leter in start:
    print(leter)
#6.2
guess_me = 7
namber = 1
while True:
    if namber < guess_me:
        print('too lov')
    elif namber==guess_me:
        print('found it!')
        break
    elif namber>guess_me:
        print('oops')
        break
    namber+=1
#6.3
guess_me = 5
for namber in range(10):
    if namber<guess_me:
        print('too lov')
    elif namber==guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break