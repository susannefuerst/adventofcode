
def find(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

def data():
    positions = []
    with open('03.inp', 'r') as inp:
        for line in inp:
            pos = find(line,'#')
            positions.append(pos)
    return positions

def trees(slope,positions):
    right = slope[0]
    down = slope[1]
    step = 0
    trees = 0
    for index in range(0,len(positions),down):
        if step in positions[index]: trees += 1
        step = (step + right) % 31
    return trees

def main():
    positions = data()
    out = 1
    for slope in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
        out *= trees(slope, positions)
    print(out)

if __name__ == '__main__':
    main()
