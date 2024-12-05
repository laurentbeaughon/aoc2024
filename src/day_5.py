def read_input(path):
    rules = []
    updates = []
    with open(path) as f:
        part_1, part_2 = f.read().split("\n\n")
        for line in part_1.splitlines():
            rules.append(line.split('|'))
        for line in part_2.splitlines():
            updates.append(line.split(','))
    return (rules, updates)


def is_correct(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


def order_update(update, rules):
    output = []
    for page in update[::-1]:
        min_index = 0
        for rule in rules:
            if page == rule[1]:
                if rule[0] in output:
                    min_index = max(output.index(rule[0]) + 1, min_index)
        output.insert(min_index, page)
    return output
            


def part_1(data, verbose):
    result = 0
    for update in data[1]:
        if is_correct(update, data[0]):
            result += int(update[len(update)//2])
    return result


def part_2(data, verbose):
    result = 0
    for update in data[1]:
        if not is_correct(update, data[0]):
            ordered_update = order_update(update, data[0])
            result += int(ordered_update[len(update)//2])
    return result


def main(data_file, verbose):
    data = read_input(data_file)
    print(part_1(data, verbose))
    print(part_2(data, verbose))
