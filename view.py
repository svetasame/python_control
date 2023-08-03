import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.choice_input)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)


def print_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")
