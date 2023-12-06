MAX_RESULTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_input():
    with open("1.in") as f:
        return f.read().splitlines()


def solve_1():
    data = get_input()
    result = 0
    for value in data:
        game_id = int(value.split(": ")[0].split(" ")[-1])
        games = value.split(": ")[-1].split(";")
        if all([is_possible(game) for game in games]):
            result += game_id
    return result


def is_possible(game):
    splitted_game = game.split(", ")
    for value in splitted_game:
        value = value.lstrip()
        count, color = value.split(" ")
        if int(count) > MAX_RESULTS[color]:
            return False
    return True


if __name__ == "__main__":
    print(solve_1())
