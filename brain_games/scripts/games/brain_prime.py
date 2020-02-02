from random import randint
import prompt


def is_num_prime(num):
    if num < 10:
        end = num
    else:
        end = 10
    for i in range(2, end):
        if num % i == 0:
            return False
    return True


def prime_game():
    num = randint(1, 50)
    correct_answer = "yes" if is_num_prime(num) else "no"
    print(f"Question: {num}")
    answer = prompt.string(prompt="Your answer: ", empty=False)
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
    "title": "Prime number game",
    "description":
        "Answer 'yes' if given number is prime. " +
        "Otherwise answer 'no'.\n",
    "game": prime_game,
}
