#!/usr/bin/env python3
import string, random
import sys

name_list = []
def new_symbol():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

def pick_random_name(name_list):
    return random.choice(name_list)

for i in range(1000):
    name_list.append(new_symbol())

for i in range(10000):
    lender = pick_random_name(name_list)
    borrower = pick_random_name(name_list)
    if lender == borrower:
        continue

    print('{lender},{borrower},{amount}'.format(lender = lender,
                                                borrower = borrower,
                                                amount = random.randint(1,999999999)))
