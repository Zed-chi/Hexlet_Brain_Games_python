from random import randint
import prompt


def calc():
    num_a = randint(0, 100)
    num_b = randint(0, 100)
    operation = randint(1, 4)
    if operation == 1:
        print(f"Question: {num_a} + {num_b}")
        result = num_a + num_b
    elif operation == 2:
        print(f"Question: {num_a} - {num_b}")
        result = num_a - num_b
    elif operation == 3:
        print(f"Question: {num_a} * {num_b}")
        result = num_a * num_b
    else:
        print(f"Question: {num_a} / {num_b}")
        result = num_a / num_b
    answer = prompt.integer(prompt="Your answer: ", empty=False)
    if answer == result:
        print("Correct!")
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. ",
            f"Correct answer was '{result}'.",
        )
        return False


game = {
    "title": "Calculation game",
    "description": "What is the result of the expression?\n",
    "game": calc,
}
