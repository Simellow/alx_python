#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", int(repr(number)[-1]))
if int(repr(number)[-1])>5: print("and is greater than 5")
if int(repr(number)[-1]) == 0: print("and is 0")
if int(repr(number)[-1])<6: print("and is less than 6 and not 0")


 



