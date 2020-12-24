#!/usr/bin/python3

def productof2(numbers,targetsum):
    complements = []
    for number in numbers:
        if number in complements:
            return number*numbers[complements.index(number)]
        complements.append(targetsum - number)
    return -1

def productof3(numbers,targetsum):
    for number in numbers:
        if number > targetsum: continue
        target = targetsum - number
        prod = productof2(numbers,target)
        if prod > -1: return number*prod
    return -1

def main(targetsum):
    with open('01.inp', 'r') as inp:
        numbers = list(map(int, inp))
    prod = productof3(numbers,targetsum)
    print(prod)


if __name__ == '__main__':
    main(2020)
