from random import randint
from prompt import integer


title = "Greatest common divider game"
rules = "Find the greatest common divisor of given numbers."
game_prompt = integer


def round():
    num_a = randint(1, 50)
    num_b = randint(1, 50)
    divider = 1
    count = 1
    while count <= min(num_a, num_b):
        if num_a % count == 0 and num_b % count == 0:
            divider = count
        count += 1
    question = f"Question: {num_a} {num_b}"
    return (question, divider)
