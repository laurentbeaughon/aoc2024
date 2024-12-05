def read_input(path):
    with open(path) as f:
        data = [
            [int(i) for i in report.split(' ')]
            for report in f.readlines()
        ]
    return data


def is_safe(report):
    diffs = [report[i] - report[i+1] for i in range(len(report) - 1)]
    return all([diff in (1, 2, 3) for diff in diffs]) or all([diff in (-1, -2, -3) for diff in diffs])


def gen_sequences(length):
    sequences = [[(i, i+1) for i in range(length - 1)]]
    for i in range(length - 1):
        sequence = []
        for j in range(length - 1):
            if j==i:
                pass
            elif j == i - 1:
                sequence.append((j, j + 2))
            else:
                sequence.append((j, j + 1))
        sequences.append(sequence)
    sequences.append([(i, i+1) for i in range(length - 2)])
    return sequences

def is_light_safe(report):
    sequences = gen_sequences(len(report))
    all_diffs = [
        [report[i] - report[j] for (i, j) in sequence]
        for sequence in sequences
    ]
    return any(
        [all([diff in (1, 2, 3) for diff in diffs]) for diffs in all_diffs]
    ) or any(
        [all([diff in (-1, -2, -3) for diff in diffs]) for diffs in all_diffs]
    )


def part_1(data, verbose):
    result = 0
    for report in data:
        if is_safe(report):
            result += 1
            if verbose:
                print(report)
    return result


def part_2(data, verbose):
    result = 0
    for report in data:
        if is_light_safe(report):
            result += 1
            if verbose:
                print(report)
    return result


def main(data_file, verbose):
    data = read_input(data_file)
    print(part_1(data, verbose))
    print(part_2(data, verbose))
