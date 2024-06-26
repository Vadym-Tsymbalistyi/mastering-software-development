# 17.5 Use ZeroMQ to publish the poem from exercise 12.4 (from Example 12-1), one
# word at a time. Write a ZeroMQ consumer that prints every word that starts with a
# vowel, and another that prints every word that contains five letters. Ignore punctuation
# characters.
import string
import zmq
from time import sleep

host = '127.0.0.1'
port = 9876
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))
print("STARTING")
sleep(10)
with open('../[Chapter 12] Processing data/mammoth.txt', 'rt') as poem:
    words = poem.read()
for word in words.split():
    word = word.strip(string.punctuation)
    data = word.encode('utf-8')
    if word.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'e', 'i', 'o', 'u')):
        print('vowels', data)
        pub.send_multipart([b'vowels', data])
    if len(word) == 5:
        print('five', data)
        pub.send_multipart([b'five', data])
sleep(3)
print('END')

