def read_input(path):
    t = []
    with open(path) as f:
        for line in f.read().splitlines():
            t.append([c for c in line])
    return t


def find_xmas(subset):
    result = 0
    if subset[3][3:] == ["X", "M", "A", "S"]:
        result += 1
    if subset[3][0:4] == ["S", "A", "M", "X"]:
        result += 1
    if [subset[i][i] for i in range(4)] == ["S", "A", "M", "X"]:
        result += 1
    if [subset[i][i] for i in range(3,7)] == ["X", "M", "A", "S"]:
        result += 1
    if [subset[6-i][i] for i in range(4)] == ["S", "A", "M", "X"]:
        result += 1
    if [subset[6-i][i] for i in range(3,7)] == ["X", "M", "A", "S"]:
        result += 1
    if [subset[i][3] for i in range(4)] == ["S", "A", "M", "X"]:
        result += 1
    if [subset[i][3] for i in range(3,7)] == ["X", "M", "A", "S"]:
        result += 1
    return result


def find_mas(subset):
    return ((subset[0][0] == "M" and subset[2][2] == "S") or (subset[0][0] == "S" and subset[2][2] == "M")) and ((subset[2][0] == "M" and subset[0][2] == "S") or (subset[2][0] == "S" and subset[0][2] == "M"))


def part_1(data, verbose):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                subset = [["." for _ in range(7)] for _ in range(7)]
                for k in range(7):
                    for l in range(7):
                        if i-3+k >= 0 and j-3+l >= 0 and i-3+k < len(data) and j-3+l < len(data[0]):
                            subset[k][l] = data[i-3+k][j-3+l]
                result += find_xmas(subset)
    return result


def part_2(data, verbose):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "A":
                subset = [["." for _ in range(3)] for _ in range(3)]
                for k in range(3):
                    for l in range(3):
                        if i-1+k >= 0 and j-1+l >= 0 and i-1+k < len(data) and j-1+l < len(data[0]):
                            subset[k][l] = data[i-1+k][j-1+l]
                if find_mas(subset):
                    result += 1
    return result


def main(data_file, verbose):
    data = read_input(data_file)
    print(part_1(data, verbose))
    print(part_2(data, verbose))
