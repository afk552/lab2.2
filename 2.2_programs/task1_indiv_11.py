#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input("Enter kWh: "))
    cost = 0
    if n <= 250:
        cost = n * 7
    elif 250 < n <= 300:
        cost = n * 17
    elif n > 300:
        cost = n * 20
    print("The final cost is:", cost)
