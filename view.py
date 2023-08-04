import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.choice_input)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)
        else:
            print(text.choice_mistake)

