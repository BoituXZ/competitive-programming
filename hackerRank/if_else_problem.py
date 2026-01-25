
import math
import os
import random
import re
import sys

def number_checker(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=5):
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    number_checker(n)

