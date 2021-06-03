#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# В списке, состоящем из целых элементов, вычислить:1) минимальный по модулю элемент списка;2) сумму модулей элементов списка, расположенных после первого элемента, равного нулю.Преобразовать список таким образом, чтобы в первой его половине располагались элементы,стоявшие в четных позициях, а во второй половине - элементы, стоявшие в нечетных позициях.



if __name__ == '__main__':
    a = list(map(float, input().split())) #1 пункт
    print("Индекс минимального элемента:", a.index(min(a)))

    def summmodul(x):  # пункт 2
        answ = 0
        mark = False
        for i in x:
            if mark:
                answ += abs(i)
            if i == 0:
                mark = True
        return answ


    def perestanovka(x):  # пункт 3
        answ = []
        try:
            for i in range(0, len(x), 2):
                answ.append(x[i])
        except IndexError:
            i = 0
        try:
            for i in range(1, len(x), 2):
                answ.append(x[i])
        except IndexError:
            i = 0
        return answ


    a = [1, 2, 3, 4, 5, 6, -7]
    b = [1, 2, 0, -3, 4, 5, 6]

    print(perestanovka(a), perestanovka(b), min(a), summmodul(a), summmodul(b), sep='\n')







