import prompt


def welcome_user():
    name = prompt.string(empty=False, prompt="May I have your name? ")
    print(f"Hello {name}")
    return name
