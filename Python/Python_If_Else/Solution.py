#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a='Weird'
    b='Not Weird'
    if 1<=n<=100:
        if n%2!=0:print(a)
        elif n%2==0 and 2<=n<=5:print(b)
        elif n%2==0 and 6<=n<=20:print(a)
        elif n%2==0 and n>20:print(b)
