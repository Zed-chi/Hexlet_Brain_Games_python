import prompt


def run(game=None, GAMES=None, answers_to_win=3):
    print("Welcome to the Brain Games!\n")
    """
    Prints Games List if games array is passed as arg,
    and waits for your choice
    """
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

    """ Executes Game round """
    print(game.rules)

    name = prompt.string(empty=False, prompt="May I have your name? ")
    print(f"Hello {name}\n")
    correct_answers = 0
    while correct_answers < answers_to_win:
        question, correct_answer = game.round()
        print(question)
        user_answer = game.game_prompt(prompt="Your Answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. ",
                f"Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return None
    print(f"Congratulations, {name}!")
    return None
