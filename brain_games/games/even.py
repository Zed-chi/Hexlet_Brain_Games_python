from random import randint


TITLE = "Even or Not"
RULES = "Answer 'yes' if number even otherwise answer 'no'."


def game_round():
    num = randint(0, 100)
    question = f"Question: {num}"
    correct_answer = "yes" if num % 2 == 0 else "no"
    return (question, correct_answer)
