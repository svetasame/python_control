import text
import view
import model


def start():
    my_notes = model.Notes()
    my_notes.load(model.NOTES_FILE)

    while True:
        choice = view.main_menu()
        if choice == 1:
            my_notes.add()
            my_notes.save(model.NOTES_FILE, text.save_successful)
        elif choice == 2:
            my_notes.edit()
        elif choice == 3:
            my_notes.delete()
        elif choice == 4:
            my_notes.list()
        elif choice == 5:
            my_notes.filter_date()
        elif choice == 6:
            break

