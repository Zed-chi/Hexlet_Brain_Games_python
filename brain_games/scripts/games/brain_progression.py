from random import randint
import prompt


PROGRESSION_LENGTH = 10


def progression_game():
    start_num = randint(1, 20)
    progression_step = randint(1, 10)
    missing_num_index = randint(1, PROGRESSION_LENGTH - 1)
    print(missing_num_index)
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

    print(f"Question: {' '.join(numbers)}")
    answer = prompt.integer(prompt="Your answer: ")
    if answer == missing_number:
        print("Correct!")
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. ",
            f"Correct answer was '{missing_number}'.",
        )
        return False


game = {
    "title": "Progression game",
    "description": "What number is missing in the progression?\n",
    "game": progression_game,
}
