# 17.4 You may have seen the classic I Love Lucy television episode in which Lucy and
# Ethel worked in a chocolate factory. The duo fell behind as the conveyor belt that
# supplied the confections for them to process began operating at an ever-faster rate.
# Write a simulation that pushes different types of chocolates to a Redis list, and Lucy is
# a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of
# chocolate. Print the time and type of each chocolate as Lucy gets it, and how many
# remain to be handled.
import redis
import random
from time import sleep

conn = redis.Redis()
name = ['milkway', 'kit-kat', 'tvix', 'random']
conveyor = 'chocolates'
print('Starting conveyor,GET TO WORK')
while True:
    seconds = random.random()
    sleep(seconds)
    piece = random.choice(name)
    conn.rpush(conveyor, piece)

