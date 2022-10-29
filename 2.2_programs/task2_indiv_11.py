#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    flag = False
    print("Enter three numbers: ")
    for i in range(3):
        a = int(input())
        if a % 2 == 0:
            flag = True
    if flag:
        print("Yes, there are some even numbers")
    else:
        print("No, there aren't any even numbers")
