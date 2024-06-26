# 16.1 Save the following text lines to a file called books.csv (notice that if the fields are
# separated by commas, you need to surround a field with quotes if it contains a
# comma):
# author,book
# J R R Tolkien,The Hobbit
# Lynne Truss,"Eats, Shoots & Leaves"
import csv

text = ''''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''
with open('books.csv', 'w') as outfile:
    outfile.write(text)

# 16.2 Use the csv module and its DictReader method to read books2.csv to the variable
# books. Print the values in books. Did DictReader handle the quotes and commas in
# the second bookвЂ™s title?
with open('books2.csv', 'r') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)

# 16.3 Create a CSV file called books2.csv by using these lines:
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China MiГ©ville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China MiГ©ville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
with open('books2.csv', 'w', encoding="utf-8") as outfile:
    outfile.write(text)

# 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table
# called books with these fields: title (text), author (text), and year (integer).
import sqlite3

db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE  IF NOT EXISTS books (title text, author text, year integer)''')
db.commit()

# 16.5 Read books.csv and insert its data into the book table.
import csv

int_str = '''insert into books values(?,?,?)'''
with open('books2.csv', 'r') as infile:
    books = csv.DictReader(infile)
    for book in books:
        cursor.execute(int_str, (book['title'], book['author'], book['year']))
db.commit()

# 16.6 Select and print the title column from the book table in alphabetical order.
sql = 'select title from books order by title asc'
for row in db.execute(sql):
    print(row)

# 16.7 Select and print all columns from the book table in order of publication.
for row in db.execute('select*from books order by year'):
    print(row)

# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you
# just made in exercise 16.4. As in 16.6, select and print the title column from the
# book table in alphabetical order.
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///books.db')
connection = engine.connect()
sql = sqlalchemy.text('SELECT title FROM books ORDER BY title ASC')
rows = connection.execute(sql)

for row in rows:
    print(row.title)

# 16.9 Install the Redis server and the Python redis library (pip install redis) on
# your computer. Create a Redis hash called test with the fields count (1) and name
# ('Fester Bestertester'). Print all the fields for test.
import redis

client = redis.StrictRedis(host='localhost', port=8080, db=0)
client.hset('test', 'count', 1)
client.hset('test', 'name', 'Fester Bestertester')

print(client.hgetall('test'))

# 16.10 Increment the count field of test and print it.
client.hincrby('test', 'count', 1)
print(client.hget('test', 'count'))
