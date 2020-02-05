from random import randint
import prompt


PROGRESSION_LENGTH = 10
title = "Progression game"
rules = "What number is missing in the progression?"
game_prompt = prompt.integer


def round():
    start_num = randint(1, 20)
    progression_step = randint(1, 10)
    missing_num_index = randint(1, PROGRESSION_LENGTH - 1)
    numbers = list(
        range(
            start_num,
            start_num + PROGRESSION_LENGTH * progression_step,
            progression_step,
        )
    )
    missing_number = numbers[missing_num_index]
    numbers[missing_num_index] = ".."
    numbers = map(lambda x: str(x), numbers)
    question = f"Question: {' '.join(numbers)}"
    return (question, missing_number)
