# TODO написать функцию, которая выдает трехзначное число
import random


def num_3():
    return int(str(random.randint(1,9)) + str(random.randint(0,9)) +
               str(random.randint(0,9)))

print(num_3())
