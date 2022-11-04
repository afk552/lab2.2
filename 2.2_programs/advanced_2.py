#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = int(input("Enter x: "))
    n = 2
    # Первый член ряда включен в результат
    result = -(x ** n / (n * math.factorial(n)))
    # Переменная отображающая смену знака
    shuffle = True
    while True:
        if x == 0:
            print("Illegal value of x", file=sys.stderr)
            exit(1)
        else:
            if not shuffle:
                n += 2
                member = x ** n / (n * math.factorial(n))
                result += -member
                shuffle = True
            else:
                n += 2
                member = x ** n / (n * math.factorial(n))
                result += member
                shuffle = False
            if math.fabs(member) < EPS:
                break
    print(result + EULER + math.log(x))
