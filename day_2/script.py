import json


DATA = json.load(open("day_2/data.json"))
BAG_MIN_PER_COLOR = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def question_1():
    sum_ids = 0
    for game_id, game_values in DATA.items():
        parsed_game = parse_game_values(game_values)
        if not has_too_many_values(parsed_game):
            sum_ids += int(game_id.split(" ")[1])

    print(f"Question 1 response is {sum_ids}")


def parse_game_values(game_values):
    parsed_game = {}
    game_sets = game_values.split(";")
    for idx, game_set in enumerate(game_sets):
        parsed_game[idx] = {}
        set_values = game_set.split(",")
        for set_value in set_values:
            value, color = set_value.strip().split(" ")
            parsed_game[idx][color] = int(value)

    return parsed_game


def has_too_many_values(parsed_game):
    for set_values in parsed_game.values():
        if any(set_values.get(color, 0) > max_value for color, max_value in BAG_MIN_PER_COLOR.items()):
            return True

    return False


def question_2():
    count = 0
    for game_id, game_values in DATA.items():
        parsed_game = parse_game_values(game_values)
        count += get_max_per_color(parsed_game)

    print(f"Question 2 response is {count}")


def get_max_per_color(parsed_game):
    power = 1
    for color in BAG_MIN_PER_COLOR:
        max_values = max(set_values.get(color, 0) for set_values in parsed_game.values())
        power *= max_values
    return power


if __name__ == '__main__':
    question_1()
    question_2()
