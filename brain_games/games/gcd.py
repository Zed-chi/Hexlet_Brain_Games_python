from random import randint


TITLE = "Greatest common divider game"
RULES = "Find the greatest common divisor of given numbers."


def game_round():
    num_a = randint(1, 50)
    num_b = randint(1, 50)
    divider = get_greatest_common_divider(num_a, num_b)
    question = f"Question: {num_a} {num_b}"
    return (question, divider)


def get_greatest_common_divider(num_a, num_b):
    divider = 1
    count = 1
    while count <= min(num_a, num_b):
        if num_a % count == 0 and num_b % count == 0:
            divider = count
        count += 1
    return divider
