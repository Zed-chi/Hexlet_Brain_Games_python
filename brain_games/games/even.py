from random import randint
import prompt


title = "Even or Not"
rules = "Answer 'yes' if number even otherwise answer 'no'."
game_prompt = prompt.string


def round():
    num = randint(0, 100)
    question = f"Question: {num}"
    correct_answer = "yes" if num % 2 == 0 else "no"
    return (question, correct_answer)
