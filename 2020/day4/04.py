#!/usr/bin/python3
import re, collections
def readblocks(file):
    blocks = []
    with open(file, 'r') as inp:
        str = inp.read()
        blocks = str.split('\n\n')
    return blocks

def todict(items):
    dict = {}
    for item in items:
        dict[item[0:3]] = item[4:]
    return dict

def main():
    blocks = readblocks("04.inp")
    valids = 0
    hairpattern = re.compile("#[0-9a-f]{6}")
    eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pidpattern = re.compile("[0-9]{9}")
    for block in blocks:
        numofitems = block.count(":")
        if numofitems < 8 and "cid:" in block: continue
        if numofitems < 7: continue
        items = block.replace("\n", " ").split(" ")
        dictitems = todict(items)
        if not 1920 <= int(dictitems["byr"]) <= 2002: continue
        if not 2010 <= int(dictitems["iyr"]) <= 2020: continue
        if not 2020 <= int(dictitems["eyr"]) <= 2030: continue
        if "cm" in dictitems["hgt"]:
            if not 150 <= int(dictitems["hgt"][:-2]) <= 193: continue
        elif "in" in dictitems["hgt"]:
            if not 59 <= int(dictitems["hgt"][:-2]) <= 76: continue
        else: continue
        if not hairpattern.fullmatch(dictitems["hcl"]): continue
        if not dictitems["ecl"] in eyecolors: continue
        if not pidpattern.fullmatch(dictitems["pid"]): continue
        valids +=1
    print(valids)

if __name__ == '__main__':
    main()
