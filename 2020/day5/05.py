#!/usr/bin/python3
import math
class Intervall:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def lower(self):
        self.b = math.floor(self.a + (self.b - self.a) / 2)

    def upper(self):
        self.a = math.ceil(self.a + (self.b - self.a) / 2)

    def converged(self):
        return self.a == self.b

    def __str__(self):
        return f"[{self.a}, {self.b}]"


def main():
    ids = []
    with open('05.inp', 'r') as inp:
        for line in inp:
            row = Intervall(0,127)
            for letter in line[0:7]:
                if letter == "F": row.lower()
                else: row.upper()
            column = Intervall(0,7)
            for letter in line[7:10]:
                if letter == "L": column.lower()
                else: column.upper()
            if row.converged() and column.converged(): ids.append(8*row.a + column.a)
            else: print('Not converged!')
    ids.sort(reverse=True)
    print(ids[0])
    for id in range(71,928):
        if not id in ids:
            print(id)
            break


if __name__ == '__main__':
    main()
