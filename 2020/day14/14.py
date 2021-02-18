#!/usr/bin/python3
import re

def clear_bit(number, position):
    mask = ~(1 << position)  # all bits on except at position
    return number & mask

def set_bit(number, position):
    mask = 1 << position  # all bits off except at position
    return number | mask

def parse_memory(line):
    pattern_str = "mem\[([0-9]+)\] = ([0-9]+)"
    pattern = re.compile(pattern_str)
    match = pattern.match(line)
    index = int(match.group(1))
    number = int(match.group(2))
    return {"index": index, "number": number}

def parse_mask(line):
    pattern_str = "mask = (.+)"
    pattern = re.compile(pattern_str)
    match = pattern.match(line)
    mask = match.group(1)
    return mask

def mask_to_dict(mask):
    off_bit_positions = [35 - index for index, letter in enumerate(mask) if letter == '0']
    on_bit_positions = [35 - index for index, letter in enumerate(mask) if letter == '1']
    floating_bit_positions = set(range(36))
    floating_bit_positions = floating_bit_positions.difference(set(off_bit_positions), set(on_bit_positions))
    return {"on": on_bit_positions, "off": off_bit_positions, "floating": list(floating_bit_positions)}

def apply_mask(number, positions):
    for pos in positions["on"]:
        number = set_bit(number, pos)
    for pos in positions["off"]:
        number = clear_bit(number, pos)
    return number

def part1(input, memory):
    with open(input, 'r') as inp:
        positions = {}
        for line in inp:
            if "mask" in line:
                mask = parse_mask(line)
                positions = mask_to_dict(mask)
            else:
                mem = parse_memory(line)
                memory[mem["index"]] = apply_mask(mem["number"], positions)
    return sum(list(memory.values()))

def part2(input, memory):
    with open(input, 'r') as inp:
        positions = {}
        for line in inp:
            if "mask" in line:
                mask = parse_mask(line)
                positions = mask_to_dict(mask)
            else:
                mem = parse_memory(line)
                n = len(positions["floating"])
                # number of possible memory addresses by setting the floatings is 2^n, iterate over them
                for num in range(1 << n):
                    on = positions["on"].copy()
                    # in part 2 the offs from the input have no effect
                    off = []
                    for i in range(n):
                        # if i-th bit is set in num add the corresponding position to the on's
                        if (num & (1 << i)) != 0:
                            on.append(positions["floating"][i])
                        else:
                            off.append(positions["floating"][i])
                    address = apply_mask(mem["index"], {"on": on, "off": off})
                    memory[address] = mem["number"]
    return sum(list(memory.values()))

if __name__ == '__main__':
    memory = {}
    print(part2('14.inp', memory))

