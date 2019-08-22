#!/usr/phthon3
'''
counter = 0
while counter < 100:
    counter += 1
    if counter % 7 == 0 or counter % 10 == 7 or counter // 10 == 7:
        continue
    print(counter, end=' ')
'''

import sys

def jump7(n):
    counter = 0
    while True:
        counter += 1
        if (counter > n):
            return
        if counter % 7 == 0 or counter % 10 == 7 or counter // 10 == 7:
            continue
        yield counter

p = jump7(100)

while True:
    try:
        print(next(p), end=" ")
    except StopIteration:
        sys.exit()
        
