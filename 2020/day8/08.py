#!/usr/bin/python3

def getbootcode(infile):
    code = []
    with open(infile, 'r') as inp:
        for line in inp:
            cline = line.strip().split(" ")
            cline.append(False)
            code.append(cline)
    return code

def main(infile):
    code = getbootcode(infile)
    accumulator = 0
    jmp = 0
    for i in range(len(code)):
        instruction = code[i + jmp]
        if instruction[2] == True: break
        instruction[2] = True
        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
        elif instruction[0] == 'jmp':
            jmp += int(instruction[1]) - 1
    print(accumulator)




if __name__ == '__main__':
    main('08.inp')
