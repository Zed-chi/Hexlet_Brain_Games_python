from random import randint
import prompt


def even_or_not():
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
            f"Correct answer was '{correct_answer}'.",
        )
        return False


game = {
    "title": "Even or Not",
    "description": "Answer 'yes' if number even otherwise answer 'no'.\n",
    "game": even_or_not,
}
