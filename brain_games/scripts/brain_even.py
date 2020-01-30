from ..cli import welcome_user
from random import randint
import prompt


def main():
    correct_answers = 0
    print("Welcome to the Brain Games!")
    print("Answer 'yes' if number even otherwise answer 'no'.\n")
    name = welcome_user()
    while correct_answers < 3:
        if ask_even_or_not():
            correct_answers += 1
    print(f"Congratulations, {name}!")
    return None


def ask_even_or_not():
    num = randint(0, 100)
    is_num_even = num % 2 == 0
    print(f"Question: {num}")
    answer = prompt.string(prompt="Your answer: ", empty=False)
    correct_answer = "yes" if is_num_even else "no"
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. ",
            f"Correct answer was '{correct_answer}'."
        )
        return False


if __name__ == "__main__":
    main()
