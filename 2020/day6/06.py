#!/usr/bin/python3
def readblocks(file):
    blocks = []
    with open(file, 'r') as inp:
        str = inp.read()
        blocks = str.split('\n\n')
    return blocks

def main():
    blocks = readblocks("06.inp")
    yes = 0
    for block in blocks:
        answers = []
        for person in block.strip('\n').split('\n'):
            answer = set()
            for letter in person:
                answer.add(letter)
            answers.append(answer)
        allyes = answers[0]
        for answer in answers[1:]:
            allyes = allyes.intersection(answer)
        yes += len(allyes)
    print(yes)


if __name__ == '__main__':
    main()
