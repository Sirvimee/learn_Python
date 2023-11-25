"""Music."""


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """

    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        self.note = note.capitalize()

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note}>"

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        alteration = {
            'A#': 'Bb', 'Bb': 'A#', 'B#': 'Cb', 'Cb': 'B#', 'C#': 'Db', 'Db': 'C#', 'D#': 'Eb', 'Eb': 'D#',
            'E#': 'Fb', 'Fb': 'E#', 'F#': 'Gb', 'Gb': 'F#', 'G#': 'Hb', 'Hb': 'G#', 'H#': 'Ib', 'Ib': 'H#',
            'I#': 'Jb', 'Jb': 'I#', 'J#': 'Kb', 'Kb': 'J#', 'K#': 'Lb', 'Lb': 'K#', 'L#': 'Mb', 'Mb': 'L#',
            'M#': 'Nb', 'Nb': 'M#', 'N#': 'Ob', 'Ob': 'N#', 'O#': 'Pb', 'Pb': 'O#', 'P#': 'Qb', 'Qb': 'P#',
            'Q#': 'Rb', 'Rb': 'Q#', 'R#': 'Sb', 'Sb': 'R#', 'S#': 'Tb', 'Tb': 'S#', 'T#': 'Ub', 'Ub': 'T#',
            'U#': 'Vb', 'Vb': 'U#', 'V#': 'Wb', 'Wb': 'V#', 'W#': 'Xb', 'Xb': 'W#', 'X#': 'Yb', 'Yb': 'X#',
            'Y#': 'Zb', 'Zb': 'Y#', 'Z#': 'Ab', 'Ab': 'Z#'
        }
        return self.note == other.note or self.note == alteration.get(other.note, other.note)

    def __lt__(self, other):
        """
        Compare notes based on their alphabetical order.

        Returns: True if the current note is alphabetically less than the other note, False otherwise.
        """
        return self.note < other.note


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.notes = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
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
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        for n in self.notes:
            if n.note == note.capitalize():
                self.notes.remove(n)
                return n
        return None

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        :return: A list of all the notes that were previously in the collection.
        """
        extracted = self.notes.copy()
        self.notes = []
        return extracted

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C#'))
          collection.add(Note('Lb'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        if len(self.notes) > 0:
            self.notes.sort()
            content = 'Notes:\n'
            for note in self.notes:
                content += f'  * {note.note}\n'
            return content.strip()
        return "Notes:\n  Empty."


class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        self.note_one = note_one
        self.note_two = note_two
        self.note_three = note_three
        self.chord_name = chord_name

        if self.note_one == self.note_two:
            raise DuplicateNoteNamesException

        if self.note_three is not None:
            if self.note_one == self.note_three or self.note_two == self.note_three:
                raise DuplicateNoteNamesException

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """
        self.chords = []

    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """
        for chord_item in self.chords:
            if chord_item.note_one == chord.note_one and chord_item.note_two == chord.note_two:
                raise ChordOverlapException
            if chord_item.note_one == chord.note_two and chord_item.note_two == chord.note_one:
                raise ChordOverlapException
            if chord_item.note_three is not None and chord.note_three is not None:
                if chord_item.note_one == chord.note_three or chord_item.note_two == chord.note_three:
                    raise ChordOverlapException

        if chord not in self.chords:
            self.chords.append(chord)

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        search = [note for note in [first_note, second_note, third_note] if note is not None]
        search.sort()

        for chord in self.chords:
            chord_notes = [note for note in [chord.note_one, chord.note_two, chord.note_three] if note is not None]
            if sorted(chord_notes) == search:
                return chord
        return None


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
    print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    print(chords.get(Note('D'), Note('Z')))  # ->  None
    chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

    chords = Chords()

    chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    chord3 = Chord(Note('E'), Note('B'), 'E5')

    chords.add(chord1)
    chords.add(chord2)
    chords.add(chord3)

    print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>

    try:
        wrong_chord = Chord(Note('E'), Note('A'), 'E')
        print('Did not raise, not working as intended.')
    except DuplicateNoteNamesException:
        print('Raised DuplicateNoteNamesException, working as intended!')

    try:
        chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
        print('Did not raise, not working as intended.')
    except ChordOverlapException:
        print('Raised ChordOverlapException, working as intended!')
