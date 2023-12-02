LETTERS_TO_NUMBER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_data():
    with open("day_1/data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def question_1():
    count = 0
    for word in get_data():
        word = clean_letters(word)
        count += get_hidden_number_in_word(word)

    print(f"Question 1 response is {count}")


def clean_letters(word):
    return word.translate({ord(i): None for i in 'azertyuiopqsdfghjklmwxcvbn'})


def get_hidden_number_in_word(row):
    if len(row) == 1:
        return int(row + row)

    return int(row[0] + row[-1])


def question_2():
    count = 0
    for word in get_data():
        word = parse_number_in_letters(word)
        word = clean_letters(word)
        count += get_hidden_number_in_word(word)

    print(f"Question 2 response is {count}")


def parse_number_in_letters(word):
    for number_in_letter, number in LETTERS_TO_NUMBER.items():
        word = word.replace(number_in_letter, f"{number_in_letter}{number}{number_in_letter}")
    return word


if __name__ == '__main__':
    question_1()
    question_2()
