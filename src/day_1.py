def read_input(path):
    left = []
    right = []
    with open(path) as f:
        for line in f.readlines():
            l, r = line.split("   ")
            left.append(int(l))
            right.append(int(r))
    return (left, right)


def part_1(data, verbose):
    left, right = data
    left.sort()
    right.sort()
    result = 0
    for l, r in zip(left, right):
        result += abs(r - l)
    return result


def part_2(data, verbose):
    left, right = data
    left.sort()
    right.sort()
    left_dict = {}
    for l in left:
        left_dict[l] = left_dict.get(l, 0) + 1
    state = 0
    result = 0
    for k, v in left_dict.items():
        appearances = 0
        while state < len(right) and right[state] <= k:
            if right[state] == k:
                appearances += 1
            state += 1
        if verbose and appearances > 0:
            print(f"{appearances} appearance of value {k} found in right series (x{v})")
        result += v * k * appearances
    return result


def main(data_file, verbose):
    data = read_input(data_file)
    print(part_1(data, verbose))
    print(part_2(data, verbose))