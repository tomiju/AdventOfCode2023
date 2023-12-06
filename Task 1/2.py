import re


def get_input():
    with open("1.in") as f:
        return f.read().splitlines()


def solve_2():
    data = get_input()
    result = 0
    for value in data:
        result += sub_solve_2(value)
    return result


def sub_solve_2(value):
    digits = []
    digit_translate = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_digit_index = -1
    last_digit_index = -1
    index = 0
    for char in value:
        if char.isdigit():
            digits.append(int(char))
            if first_digit_index == -1:
                first_digit_index = index
            last_digit_index = index
        index += 1
    for _dig_val in digit_translate:
        if _dig_val in value:
            if first_digit_index < 0 or first_digit_index > value.index(_dig_val):
                first_digit_index = value.index(_dig_val)
                digits = [digit_translate.index(_dig_val) + 1] + digits
            tmp_digit = [m.start() for m in re.finditer(_dig_val, value)][-1]
            if last_digit_index < 0 or last_digit_index < tmp_digit:
                last_digit_index = tmp_digit
                digits.append(digit_translate.index(_dig_val) + 1)
    if digits:
        return int(str(digits[0]) + str(digits[-1]))
    return 0


if __name__ == "__main__":
    # print(sub_solve_2("fiveeight792eightqskstrfninesrgfivec"))
    print(solve_2())
#
