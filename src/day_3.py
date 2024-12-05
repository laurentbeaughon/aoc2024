import re


def read_input(path):
    with open(path) as f:
        return f.readlines()


def part_1(data, verbose):
    result = 0
    for line in data:
        matches = re.finditer(r"mul\((\d+),(\d+)\)", line)
        for match in matches:
            
            result += int(match.group(1)) * int(match.group(2))
    return result


def part_2(data, verbose):
    result = 0
    do = True
    for line in data:
        matches = re.finditer(r"mul\((\d+),(\d+)\)|do(n't)?", line)
        for match in matches:
            if do and match.group()[0] == "m":
                result += int(match.group(1)) * int(match.group(2))
            elif match.group() == "do":
                do = True
            elif match.group() == "don't":
                do = False
    return result


def main(data_file, verbose):
    data = read_input(data_file)
    print(part_1(data, verbose))
    print(part_2(data, verbose))
