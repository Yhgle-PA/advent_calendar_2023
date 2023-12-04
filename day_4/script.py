import json


DATA = json.load(open("day_4/data.json"))


def question_1():
    count = 0
    for _, game_values in DATA.items():
        winning_numbers, has_numbers = parse_game(game_values)
        count += points_per_card(winning_numbers, has_numbers)

    print(f"Question 1 response is {count}")


def parse_game(game_values):
    winning_numbers, has_numbers = game_values.split("|")
    winning_numbers = [num.strip() for num in winning_numbers.split(" ") if num.strip() != '']
    has_numbers = [num.strip() for num in has_numbers.split(" ") if num.strip() != '']
    return winning_numbers, has_numbers


def points_per_card(winning_numbers, has_numbers):
    length_correct_numbers = length_win_numbers(winning_numbers, has_numbers)
    if length_correct_numbers == 0:
        return 0
    return 2**(length_correct_numbers - 1)


def length_win_numbers(winning_numbers, has_numbers):
    return len([num for num in has_numbers if num in winning_numbers])


def question_2():
    count_per_card = [1 for _ in DATA]
    for idx_card, (_, game_values) in enumerate(DATA.items()):
        winning_numbers, has_numbers = parse_game(game_values)
        number_win = length_win_numbers(winning_numbers, has_numbers)
        for idx_win in range(number_win):
            count_per_card[idx_card + 1 + idx_win] += count_per_card[idx_card]

    print(f"Question 2 response is {sum(count_per_card)}")


if __name__ == '__main__':
    question_1()
    question_2()
