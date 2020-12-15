#!/usr/bin/python3

def getrules():
    rules = {}
    with open('07.inp', 'r') as inp:
        for line in inp:
            tmp = line.split(" bags contain ")
            bag = tmp[0]
            tmp = tmp[1].replace(".\n", "").split(", ")
            content = {}
            for entry in tmp:
                tmp2 = entry.split(" ")
                key = f"{tmp2[1]} {tmp2[2]}"
                content[key] = tmp2[0]
            rules[bag] = content
    return rules

def getbags(color, rules):
    bags = []
    for key in rules:
        if color in list(rules[key].keys()):
            bags.append(key)
            bags.extend(getbags(key,rules))
    return set(bags)

def getcontent(color, rules):
    count = 1
    for key in rules:
        if color == key:
            for othercol in list(rules[key].keys()):
                content = int(rules[key][othercol].replace("no","0"))
                count += content*getcontent(othercol,rules)
    return count

def main():
    rules = getrules()
    print(len(getbags("shiny gold",rules)))
    print(getcontent("shiny gold",rules) - 1)

if __name__ == '__main__':
    main()
