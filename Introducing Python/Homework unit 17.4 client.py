# 17.4 You may have seen the classic I Love Lucy television episode in which Lucy and
# Ethel worked in a chocolate factory. The duo fell behind as the conveyor belt that
# supplied the confections for them to process began operating at an ever-faster rate.
# Write a simulation that pushes different types of chocolates to a Redis list, and Lucy is
# a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of
# chocolate. Print the time and type of each chocolate as Lucy gets it, and how many
# remain to be handled.
import redis
from datetime import datetime
from time import sleep

conn = redis.Redis()
timeout = 10
conveyor = 'chocolates'
print('Laci in work')
while True:
    sleep(0.1)
    msg = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if msg:
        piece = msg[1]
        print('Lucy got a', piece, 'at', datetime.utcnow(), 'only', remaining, 'left')

