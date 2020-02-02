from ..cli import welcome_user
from random import randint
import prompt


def main():
    correct_answers = 0
    print("Welcome to the Brain Games!")
    print("What is the result of the expression?\n")
    name = welcome_user()
    while correct_answers < 3:
        if ask_expression():
            correct_answers += 1
    print(f"Congratulations, {name}!")
    return None


def ask_expression():
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


if __name__ == "__main__":
    main()
