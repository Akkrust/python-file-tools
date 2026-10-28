from pathlib import Path

folder = Path(r"C:\Users\PC\Downloads")

search = input("What are you looking for? ").lower().strip()
suffix = input("File extension: ").lower().strip()

count = 0
results = []

if not folder.is_dir():
    print("Error: The search folder was not found!")

elif not search:
    print("Error: Please enter a filename or part of a filename!")

elif not suffix or not suffix.strip("."):
    print("Error: Please enter a file extension!")

else:
    suffix = "." + suffix.lstrip(".")

    for file in folder.rglob("*"):
        if (
            file.is_file()
            and search in file.name.lower()
            and file.suffix.lower() == suffix
        ):
            count += 1
            results.append(file)
            print(file.name)

    if count == 0:
        print("No files matched your search criteria.")
    else:
        print("Files found:", count)

    with open("result.txt", "w", encoding="utf-8") as file:
        file.write("FILE SEARCH REPORT\n\n")
        file.write("Search query: " + search + "\n")
        file.write("File extension: " + suffix + "\n\n")
        file.write("Matching files:\n\n")

        if results:
            for el in results:
                file.write(str(el) + "\n")
        else:
            file.write("No matching files were found.\n")

