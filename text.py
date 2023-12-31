
main_menu = '''\nГлавное меню:
    1. Добавить заметку
    2. Редактировать заметку
    3. Удалить заметку
    4. Вывести список заметок
    5. Фильтровать заметки по дате
    6. Выход\n'''

choice_input = "Введите номер команды: "

choice_mistake = "Неверный номер команды."

ID = "Введите номер ID:"

tittle_input = "Введите заголовок заметки: "

new_tittle_input = "Введите новый заголовок заметки (оставьте пустым, чтобы не изменять): "

note_input = "Введите текст заметки: "

new_note_input = "Введите новый текст заметки (оставьте пустым, чтобы не изменять): "

date_start_input = "Введите начальную дату (в формате дд.мм.гггг): "

date_end_input = "Введите конечную дату (в формате дд.мм.гггг): "

date_mistake = "Нет заметок, удовлетворяющих заданному диапазону дат."

value_date_error = "Неверный формат даты. Введите в формате дд.мм.гггг"

save_successful = "Заметка успешно сохранена."

change_successful = "Заметка успешно отредактирована."

delete_successful = "Заметка успешно удалена."

no_notes = "Нет доступных заметок."

all_notes = "Список доступных заметок:"

date_notes = "Список заметок, удовлетворяющих заданному диапазону дат:"

find_input = "Введите номер заметки, которую хотите отредактировать: "

delete_input = "Введите номер заметки, которую хотите удалить: "

find_mistake = "Неверный номер заметки."


def change_note_name (note: str) -> str:
    return f"Редактирование заметки: {note['title']}"


def create_stamp (note: str) -> str:
    return f"Создано: {note['timestamp']}"




