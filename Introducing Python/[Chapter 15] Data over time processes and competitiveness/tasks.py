# 15.1. Use multiprocessing to create three separate processes. Make each one wait a
# random number of seconds between zero and one, print the current time, and then
# exit.
import multiprocessing


def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print(seconds, datetime.today())


if __name__ == '__main__':
    import random

    for n in range(3):
        seconds = random.random()
        process = multiprocessing.Process(target=now, args=(seconds,))
        process.start()