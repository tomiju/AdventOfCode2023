def get_input():
    with open("1.in") as f:
        return f.read().splitlines()


def solve_1():
    data = get_input()
    result = 0
    for value in data:
        result += sub_solve_1(value)
    return result


def sub_solve_1(value):
    digits = []
    for char in value:
        if char.isdigit():
            digits.append(int(char))
    if digits:
        return int(str(digits[0]) + str(digits[-1]))
    return 0


if __name__ == "__main__":
    print(solve_1())
