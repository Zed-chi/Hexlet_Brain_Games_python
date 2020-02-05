from random import randint
from prompt import integer

title = "Calculation game"
rules = "What is the result of the expression?"
game_prompt = integer


def round():
    num_a = randint(0, 100)
    num_b = randint(0, 100)
    operation = randint(1, 4)
    if operation == 1:
        question = f"Question: {num_a} + {num_b}"
        result = num_a + num_b
    elif operation == 2:
        question = f"Question: {num_a} - {num_b}"
        result = num_a - num_b
    elif operation == 3:
        question = f"Question: {num_a} * {num_b}"
        result = num_a * num_b
    else:
        question = f"Question: {num_a} // {num_b}"
        result = num_a // num_b
    return (question, result)
