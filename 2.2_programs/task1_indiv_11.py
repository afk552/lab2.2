#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input("Enter kWh: "))
    cost = 0
    k1 = 7
    k2 = 17
    k3 = 20
    if n <= 250:
        cost = n * k1
    elif n <= 300:
        cost = k1*250+(n-250)*k2
    else:
        cost = k1*250+k2*300+(n-300)*k3
    print("The final cost is:", cost)
