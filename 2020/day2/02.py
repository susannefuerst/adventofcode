#!/usr/bin/python3
import re
def data():
    pattern = re.compile('([0-9]{1,2})-([0-9]{1,2}) ([a-z]): (.*)')
    with open('02.inp', 'r') as inp:
        datalist = []
        for line in inp:
            dict = {}
            m = pattern.match(line)
            dict["lower"] = int(m.group(1))
            dict["upper"] = int(m.group(2))
            dict["letter"] = m.group(3)
            dict["pw"] = m.group(4)
            datalist.append(dict)
    return datalist

def valid(dict):
    count = dict["pw"].count(dict["letter"])
    if dict["lower"] <= count and count <= dict["upper"]:
        return 1
    return 0

def find(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

def valid2(dict):
    indices = find(dict["pw"],dict["letter"])
    if (dict["lower"]-1 in indices) ^ (dict["upper"]-1 in indices):
        return 1
    return 0


if __name__ == '__main__':
    dat = data()
    valids = 0
    for dict in dat:
        valids += valid2(dict)
    print(valids)
