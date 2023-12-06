MAX_RESULTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_input():
    with open("1.in") as f:
        return f.read().splitlines()


def solve_2():
    data = get_input()
    result = 0
    for value in data:
        games = value.split(": ")[-1].split(";")
        result += get_max_for_game(games)
    return result


def is_game_possible(game):
    splitted_game = game.split(", ")
    for value in splitted_game:
        value = value.lstrip()
        count, color = value.split(" ")
        if int(count) > MAX_RESULTS[color]:
            return False
    return True


def get_max_for_game(games):
    max_color_values = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for game in games:
        splitted_game = game.split(", ")
        for value in splitted_game:
            value = value.lstrip()
            count, color = value.split(" ")
            count = int(count)
            if count > max_color_values[color]:
                max_color_values[color] = count
    return max_color_values["red"] * max_color_values["green"] * max_color_values["blue"]


if __name__ == "__main__":
    print(solve_2())
