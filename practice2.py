
import random
import time

def randomTimes(averagesecondsbetweencalls):
    print(random.gauss(averagesecondsbetweencalls, 60*1))
    return random.gauss(averagesecondsbetweencalls, 60*1)
