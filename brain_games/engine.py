import prompt


def run(game=None, answers_to_win=3):
    if game is None:
        return
    print("Welcome to the Brain Games!")
    print(game.rules, "\n")

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
            return
    print(f"Congratulations, {name}!")
