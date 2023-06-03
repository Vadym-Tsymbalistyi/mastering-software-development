# 14.1 List the files in your current directory.
import os

path = '.'
print(os.listdir(path))
# 14.2 List the files in your parent directory.
import os

print(os.listdir('..'))
# 14.3 Assign the string 'This is a test of the emergency text system' to the
# variable test1, and write test1 to a file called test.txt.
test1 = 'This is a test of the emergency text system'
len(test1)
with open('test.txt', 'wt') as outfile:
    print(outfile.write(test1))
# 14.4 Open the file test.txt and read its contents into the string test2. Are test1 and
# test2 the same?
with open('test.txt', 'rt') as infile:
    test2 = infile.read()
    print(len(test2))
    print(test1 == test2)