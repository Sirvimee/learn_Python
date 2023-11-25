"""Music."""


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """
    def __init__(self, note: str):
        self.note = note.capitalize()

    def __repr__(self) -> str:
        return f"<Note: {self.note}>"

    def __eq__(self, other):
        alteration = {
            'A#': 'Bb', 'Bb': 'A#', 'B#': 'Cb', 'Cb': 'B#', 'C#': 'Db', 'Db': 'C#', 'D#': 'Eb', 'Eb': 'D#',
            'E#': 'Fb', 'Fb': 'E#', 'F#': 'Gb', 'Gb': 'F#', 'G#': 'Ab', 'Ab': 'G#', 'H#': 'Ib', 'Ib': 'H#',
            'I#': 'Jb', 'Jb': 'I#', 'J#': 'Kb', 'Kb': 'J#', 'K#': 'Lb', 'Lb': 'K#', 'L#': 'Mb', 'Mb': 'L#',
            'M#': 'Nb', 'Nb': 'M#', 'N#': 'Ob', 'Ob': 'N#', 'O#': 'Pb', 'Pb': 'O#', 'P#': 'Qb', 'Qb': 'P#',
            'Q#': 'Rb', 'Rb': 'Q#', 'R#': 'Sb', 'Sb': 'R#', 'S#': 'Tb', 'Tb': 'S#', 'T#': 'Ub', 'Ub': 'T#',
            'U#': 'Vb', 'Vb': 'U#', 'V#': 'Wb', 'Wb': 'V#', 'W#': 'Xb', 'Xb': 'W#', 'X#': 'Yb', 'Yb': 'X#',
            'Y#': 'Zb', 'Zb': 'Y#', 'Z#': 'Ab', 'Ab': 'Z#'
        }
        return self.note == other.note or self.note == alteration.get(other.note, other.note)

    def __lt__(self, other):
        return self.note < other.note


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        self.notes = []

    def add(self, note: Note) -> None:
        if not isinstance(note, Note):
            raise TypeError("Added object is not an instance of Note.")
        if len(note.note) == 1:
            if note not in self.notes:
                self.notes.append(note)
        if len(note.note) == 2:
            equivalent_found = any(note.__eq__(n) for n in self.notes) or note in self.notes
            if not equivalent_found:
                self.notes.append(note)

    def pop(self, note: str) -> Note | None:
        for n in self.notes:
            if n.note == note.capitalize():
                self.notes.remove(n)
                return n
        return None

    def extract(self) -> list[Note]:
        extracted = self.notes.copy()
        self.notes = []
        return extracted

    def get_content(self) -> str:
        if len(self.notes) > 0:
            self.notes.sort()
            content = 'Notes:\n'
            for note in self.notes:
                content += f'  * {note.note}\n'
            return content.strip()
        return "Notes:\n  Empty."


if __name__ == '__main__':
    note_one = Note('a')  # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
    collection = NoteCollection()

    print(note_one)  # <Note: A>
    print(note_three)  # <Note: Eb>

    collection.add(note_one)
    collection.add(note_two)

    print(collection.get_content())
    # Notes:
    #   * A
    #   * C

    print(collection.extract())  # [<Note: A>,<Note: C>]
    print(collection.get_content())
    # Notes:
    #  Empty

    collection.add(note_one)
    collection.add(note_two)
    collection.add(note_three)

    print(collection.pop('a') == note_one)  # True
    print(collection.pop('Eb') == note_three)  # True
