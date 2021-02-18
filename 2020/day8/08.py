#!/usr/bin/python3

def getbootcode(infile):
    code = []
    with open(infile, 'r') as inp:
        for line in inp:
            cline = line.strip().split(" ")
            cline.append(False)
            code.append(cline)
    return code

def runcode(code):
    accumulator = 0
    jmp = 0
    for i in range(len(code)):
        if i + jmp >= len(code):
            return [True, accumulator]
        instruction = code[i + jmp]
        if instruction[2] == True:
            return [False, accumulator]
        instruction[2] = True
        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
        elif instruction[0] == 'jmp':
            jmp += int(instruction[1]) - 1
    return [True, accumulator]

def fixcode(code):
    i = 0
    result = runcode(code)
    while not result[0]:
        code = getbootcode('08.inp')
        if code[i][0] == "nop" and int(code[i][1]) != 0:
            code[i][0] = "jmp"
        if code[i][0] == "jmp":
            code[i][0] = "nop"
        i += 1
        if i == len(code):
            print("Could not fix code")
            break
        result = runcode(code)
    return result[1]

def printcode(code):
    for i in range(len(code)):
        print(code[i])

if __name__ == '__main__':
    code = getbootcode('08.inp')
    print(runcode(code)[1])
    print(fixcode(code))
