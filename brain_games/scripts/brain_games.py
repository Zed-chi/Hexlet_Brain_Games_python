import prompt


def welcome_user():
    name = prompt.string(empty=False, prompt="May I have your name? ")
    print(f"Hello {name}")
    return name


def main(game=None, GAMES=None, ANSWERS_TO_WIN=3):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    if game is None and GAMES is None:
        return None
    elif game is None and GAMES:
        print("Available Games: ")
        for i, v in enumerate(GAMES):
            print(f"{i}. {v['title']}")

        choice = None
        while choice is None or choice > len(GAMES) - 1 or choice < 0:
            choice = prompt.integer(prompt="Your choice: ")
        game = GAMES[choice]

    print(game["description"])
    correct_answers = 0
    while correct_answers < ANSWERS_TO_WIN:
        if game["game"]():
            correct_answers += 1
    print(f"Congratulations, {name}!")
    return None
