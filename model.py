import json
import datetime
import text

NOTES_FILE = "notes.json"


class Note:
    def __init__(self, note_id, tittle, message, timestamp=None):
        self.note_id = note_id
        self.tittle = tittle
        self.message = message
        self.timestamp = timestamp or datetime.datetime.now().isoformat()

    def to_dict(self):
        return {"note_id": self.note_id,
                "tittle": self.tittle,
                "text": self.message,
                "data": self.timestamp
                }

    def to_json(self):
        return json.dump(self.to_dict())

    @classmethod
    def from_dict(cls, note_dict):
        return cls(
            note_id=note_dict["note_id"],
            tittle=note_dict["tittle"],
            message=note_dict["text"],
            timestamp=note_dict["data"]
        )

    @classmethod
    def from_json(cls, note_json):
        note_dict = json.loads(note_json)
        return cls.from_dict(note_dict)


class Notes:

    def __init__(self):
        self.notes = []
        self.note_id = 1

    def add(self):
        self.note_id += 1
        tittle = input(text.tittle_input)
        message = input(text.note_input)
        timestamp = datetime.datetime.now().isoformat()
        note = {"note_id": self.note_id, "tittle": tittle, "text": message, "data": timestamp}
        self.notes.append(note)

    def delete(self):
        note_id = input(text.delete_input)
        existing_note = next((note for note in self.get_note()
                              if note["note_id"] == note_id), None)
        if existing_note:
            self.notes = [note for note in self.get_note() if note["note_id"] != note_id]
            self.save(NOTES_FILE, text.delete_successful)
        else:
            print(text.find_mistake)

    def filter_date(self):
        start_date = input(text.date_start_input)
        end_date = input(text.date_end_input)
        try:
            start_datetime = datetime.datetime.strptime(start_date, "%d.%m.%Y")
            end_datetime = datetime.datetime.strptime(end_date, "%d.%m.%Y")

            filtered_notes = [note for note in self.get_note()
                              if start_datetime <=
                              datetime.datetime.strptime(note["data"],
                                                         "%Y-%m-%dT%H:%M:%S") <= end_datetime]
            if filtered_notes:
                for note in filtered_notes:
                    print(f"ID:{note['note_id']}")
                    print(f"Tittle:{note['tittle']}")
                    print(f"Text:{note['text']}")
                    print(f"Data:{note['data']}")
                    print()
            else:
                print(text.date_mistake)
        except ValueError:
            print(text.value_date_error)

    def get_note(self):
        return self.notes

    def edit(self):
        note_id = input(text.find_input)

        existing_note = next((note for note in self.get_note()
                              if note["note_id"] == note_id), None)
        if existing_note:
            tittle = input(text.new_tittle_input)
            message = input(text.new_note_input)
            if tittle:
                existing_note["tittle"] = tittle
            if message:
                existing_note["text"] = message
            existing_note["data"] = datetime.datetime.now().isoformat()
            self.save(NOTES_FILE, text.change_successful)
        else:
            print(text.find_mistake)

    def list(self):
        all_notes = self.get_note()
        if all_notes:
            print(text.all_notes)
            for note in all_notes:
                print(f"ID:{note['note_id']}")
                print(f"Tittle:{note['tittle']}")
                print(f"Text:{note['text']}")
                print(f"Data:{note['data']}")
                print()
        else:
            print(text.no_notes)

    def save(self, path, message_for_print):
        with open(path, "w") as file:
            json.dump(self.notes, file, indent=4)
        print(message_for_print)

    def load(self, path):
        try:
            with open(path, "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []


