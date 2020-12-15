def find(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

def readblocks(file):
    blocks = []
    with open(file, 'r') as inp:
        str = inp.read()
        blocks = str.split('\n\n')
    return blocks

if __name__ == '__main__':
    print(readblocks("day4/04.inp"))
