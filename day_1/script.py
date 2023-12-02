def get_data():
    with open("day_1/data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def question_1():
    count = 0
    data = get_data()
    data_clean = clean_letters(data)
    for row in data_clean:
        count += count_one_line(row)

    print(f"Question 1 response is {count}")


def clean_letters(data):
    return [s.translate({ord(i): None for i in 'azertyuiopqsdfghjklmwxcvbn'}) for s in data]


def count_one_line(row):
    if len(row) == 1:
        return int(row + row)

    return int(row[0] + row[-1])


def question_2():
    count = 0
    data = get_data()
    data_clean = parse_number_in_letters(data)
    data_clean = clean_letters(data_clean)
    for row in data_clean:
        count += count_one_line(row)

    print(f"Question 2 response is {count}")


def parse_number_in_letters(data):
    return [w.replace("one", "o1e")
             .replace("two", "t2o")
             .replace("three", "t3e")
             .replace("four", "f4r")
             .replace("five", "f5e")
             .replace("six", "s6x")
             .replace("seven", "s7n")
             .replace("eight", "e8t")
             .replace("nine", "n9e") for w in data]


if __name__ == '__main__':
    question_1()
    question_2()
