def write_note(notes):
    file = open('notes.txt', 'wt')
    file.writelines(notes)
    file.close()

def read_note():
    file = open('notes.txt', 'rt')
    notes = file.readlines()
    file.close()
    return notes

from pathlib import Path

file_path = Path("notes.txt")

if not file_path.is_file():
    notes = []
    write_note(notes)

# Create
# Read
# Update
# Delete
while True:
    notes = read_note()
    command = str(input("Enter a command : "))
    # Create
    if command == "c1":
        # 1
        note = str(input("Enter a note: "))
        notes.append(f"{note}\n")
    elif command == "c2":
        # 2
        note = str(input("Enter a note: "))
        notes.insert(0, f"{note}\n")
    # Read
    elif command == "r1":
        # 1
        for note in notes:
            print(note,end="")
    elif command == "r2":
        # 2
        for i in range(len(notes)):
            print(i, notes[i],end="")
    # Update
    elif command == "u1":
        # 1
        index = int(input("Enter a index : "))
        new_note = str(input("Enter a new note : "))
        notes[index] = f"{new_note}\n"
    elif command == "u2":
        # 2 По повному збігу старого напису
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                notes[i] = f"{new_note}\n"
    elif command == "u3":
        # 3 По частковому збігу старого напису
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                notes[i] = f"{new_note}\n"
                # Delete
    elif command == "d1":
        # 1
        index = int(input("Enter a index : "))
        del notes[index]
    elif command == "d2":
        # 2 По повному збігу старого напису
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                del notes[i]
    elif command == "d3":
        # 3 По частковому збігу старого напису
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                del notes[i]
    write_note(notes)