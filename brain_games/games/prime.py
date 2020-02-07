from random import randint


TITLE = "Prime number game"
RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_num_prime(num):
    if num < 10:
        end = num
    else:
        end = 10
    for i in range(2, end):
        if num % i == 0:
            return False
    return True


def game_round():
    num = randint(1, 50)
    correct_answer = "yes" if is_num_prime(num) else "no"
    question = f"Question: {num}"
    return (question, correct_answer)
