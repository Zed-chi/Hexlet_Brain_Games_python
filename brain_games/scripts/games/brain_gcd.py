from random import randint
import prompt


def greatest_common_divider_game():
    num_a = randint(1, 50)
    num_b = randint(1, 50)
    divider = 1
    count = 1
    while count <= min(num_a, num_b):
        if num_a % count == 0 and num_b % count == 0:
            divider = count
        count += 1

    print(f"Question: {num_a} {num_b}")
    answer = prompt.integer(prompt="Your answer: ")
    if answer == divider:
        print("Correct!")
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. ",
            f"Correct answer was '{divider}'.",
        )
        return False


game = {
    "title": "Greatest common divider game",
    "description": "Find the greatest common divisor of given numbers.\n",
    "game": greatest_common_divider_game,
}
