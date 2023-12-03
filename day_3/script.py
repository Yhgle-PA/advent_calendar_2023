def get_data():
    with open("day_3/data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def question_1():
    count = 0
    data = get_data()
    parsed_data = parse_data_question_1(data)
    for (start_idx_x, end_idx_x, idx_y), value in parsed_data["number_coord"].items():
        if is_close_to_a_symbol(start_idx_x, end_idx_x, idx_y, parsed_data["symbol_coord"]):
            count += value

    print(f"Question 1 response is {count}")


def parse_data_question_1(data):
    parsed_data = {"number_coord": {}, "symbol_coord": []}
    for idx_y, row in enumerate(data):
        idx_x = 0
        while idx_x < len(row):
            if row[idx_x] == ".":
                idx_x += 1
            elif row[idx_x].isdigit():
                start_idx_x, end_idx_x, value = find_number_coord(idx_x, row)
                parsed_data["number_coord"][(start_idx_x, end_idx_x, idx_y)] = value
                idx_x = end_idx_x + 1
            else:
                parsed_data["symbol_coord"].append((idx_x, idx_y))
                idx_x += 1

    return parsed_data


def find_number_coord(start_idx_x, row):
    current_idx_x = start_idx_x + 1
    while current_idx_x != len(row) and row[current_idx_x].isdigit():
        current_idx_x += 1

    value = int(row[start_idx_x:current_idx_x])
    return start_idx_x, current_idx_x - 1, value


def is_close_to_a_symbol(start_idx_x, end_idx_x, idx_y, symbol_coord):
    for symbol_idx_x, symbol_idx_y in symbol_coord:
        if symbol_and_number_are_adjacent(start_idx_x, end_idx_x, idx_y, symbol_idx_x, symbol_idx_y):
            return True

    return False


def symbol_and_number_are_adjacent(start_idx_x, end_idx_x, idx_y, symbol_idx_x, symbol_idx_y):
    return abs(symbol_idx_y - idx_y) <= 1 and (start_idx_x - 1 <= symbol_idx_x <= end_idx_x + 1)


def question_2():
    count = 0
    data = get_data()
    parsed_data = parse_data_question_2(data)
    for symbol_idx_x, symbol_idx_y in parsed_data["symbol_coord"]:
        numbers_close_to_symbol = values_close_to_symbol(symbol_idx_x, symbol_idx_y, parsed_data["number_coord"])
        if len(numbers_close_to_symbol) == 2:
            count += numbers_close_to_symbol[0] * numbers_close_to_symbol[1]

    print(f"Question 2 response is {count}")


def parse_data_question_2(data):
    parsed_data = {"number_coord": {}, "symbol_coord": []}
    for idx_y, row in enumerate(data):
        idx_x = 0
        while idx_x < len(row):
            if row[idx_x] == "*":
                parsed_data["symbol_coord"].append((idx_x, idx_y))
                idx_x += 1
            elif row[idx_x].isdigit():
                start_idx_x, end_idx_x, value = find_number_coord(idx_x, row)
                parsed_data["number_coord"][(start_idx_x, end_idx_x, idx_y)] = value
                idx_x = end_idx_x + 1
            else:
                idx_x += 1

    return parsed_data


def values_close_to_symbol(symbol_idx_x, symbol_idx_y, number_coord):
    values_close_to_symbol = []
    for (start_idx_x, end_idx_x, idx_y), value in number_coord.items():
        if symbol_and_number_are_adjacent(start_idx_x, end_idx_x, idx_y, symbol_idx_x, symbol_idx_y):
            values_close_to_symbol.append(value)

    return values_close_to_symbol


if __name__ == '__main__':
    question_1()
    question_2()
