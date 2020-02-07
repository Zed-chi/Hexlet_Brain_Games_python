from random import randint, choice


TITLE = "Calculation game"
RULES = "What is the result of the expression?"


def game_round():
    num_a = randint(0, 100)
    num_b = randint(0, 100)
    operation_char, operation = choice(
        ("+", int.__add__),
        ("-", int.__sub__),
        ("*", int.__mul__),
        ("//", int.__floordiv__),
    )
    question = f"Question: {num_a} {operation_char} {num_b}"
    result = operation(num_a,  num_b)
    return (question, result)
