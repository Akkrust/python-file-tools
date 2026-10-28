import shutil
from pathlib import Path

folder = Path(r"C:\Users\PC\Downloads")

destinations = {
    ".pdf": folder / "PDF",
    ".docx": folder / "documents",
    ".zip": folder / "ARCHIVE"
}

moved = 0
skipped = 0
conflicts = 0
errors = 0

for el in folder.iterdir():
    if not el.is_file():
        continue

    suffix = el.suffix.lower()
    destination_folder = destinations.get(suffix)

    if destination_folder is None:
        skipped += 1
        continue

    destination_folder.mkdir(parents=True, exist_ok=True)

    destination = destination_folder / el.name

    if destination.exists():
        print("File already exists:", el.name)
        conflicts += 1
        continue

    try:
        shutil.move(el, destination)
        moved += 1
    except OSError as error:
        errors += 1
        print("Failed to move file:", el.name, "| Error:", error)

print("File sorting completed!")
print("Files moved:", moved)
print("Files skipped:", skipped)
print("Filename conflicts:", conflicts)
print("Errors:", errors)