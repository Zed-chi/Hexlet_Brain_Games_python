import prompt


def run():
    name = prompt.string('\nMay I have your name? ')
    print("Hello, {}!".format(name))


if __name__ == "__main__":
    run()
