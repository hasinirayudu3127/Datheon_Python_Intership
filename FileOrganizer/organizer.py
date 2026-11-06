import shutil
from pathlib import Path

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"]
}


def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    if not destination.exists():
        return destination

    folder = destination.parent
    name = destination.stem
    extension = destination.suffix
    count = 1

    while True:
        new_path = folder / f"{name}_{count}{extension}"

        if not new_path.exists():
            return new_path

        count += 1


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: Invalid folder path.")
        return

    moved = 0
    failed = 0

    for file in list(folder.iterdir()):

        if not file.is_file():
            continue

        category = get_category(file)
        category_folder = folder / category

        try:
            category_folder.mkdir(exist_ok=True)

            destination = get_unique_path(
                category_folder / file.name
            )

            shutil.move(str(file), str(destination))

            print(f"Moved: {file.name} -> {category}")
            moved += 1

        except PermissionError:
            print(f"Permission denied: {file.name}")
            failed += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")
            failed += 1

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files moved successfully: {moved}")
    print(f"Files failed: {failed}")
    print("File organization completed!")


if __name__ == "__main__":
    print("===== AUTOMATED FILE ORGANIZER =====")

    folder_path = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    organize_files(folder_path)