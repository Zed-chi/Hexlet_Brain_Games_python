from random import randint
from math import sqrt


TITLE = "Prime number game"
RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_num_prime(num):
    for i in range(2, sqrt(num)):
        if num % i == 0:
            return False
    return True


def game_round():
    num = randint(2, 50)
    correct_answer = "yes" if is_num_prime(num) else "no"
    question = f"Question: {num}"
    return (question, correct_answer)
