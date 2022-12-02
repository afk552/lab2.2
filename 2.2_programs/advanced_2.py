#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Введите x: "))
    if x == 0:
        print("Неверно задан X", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    # Сумма членов ряда
    while math.fabs(a) > EPS:
        a *= -1*x**2*(2*n)/(2*n+2)**2
        S += a
        n += 1
    # Значение функции
    print(f"Сi({x}) = {EULER + math.log(math.fabs(x)) + S}")
