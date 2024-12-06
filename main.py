import csv
import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")


def load_document_types(csv_path):
    document_types = {}
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            document_types[row["pattern"]] = row["destination"]
    return document_types


def load_extensions(csv_path):
    extensions = {}
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            extensions[row["extension"]] = row["folder"]
    return extensions


def MoveBasedOnDocumentType(
    directory: str, document_types, file_path: str, filename: str
):
    for document_type in document_types:
        if document_type in filename:
            folder_name = document_types[document_type]
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {folder_name}")


def MoveBasedOnExtension(
    directory: str,
    extensions: dict,
    document_types: dict,
    file_path: str,
    filename: str,
):
    extension = os.path.splitext(file_path)[1].lower()

    if extension in extensions:
        MoveBasedOnDocumentType(directory, document_types, file_path, filename)
    else:
        print(f"Skipping {filename}")


def main():
    # Load both CSV files
    base_dir = os.path.dirname(__file__)
    document_types = load_document_types(
        os.path.join(base_dir, "document_mappings.csv")
    )
    extensions = load_extensions(os.path.join(base_dir, "extension_mappings.csv"))

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            MoveBasedOnExtension(
                directory, extensions, document_types, file_path, filename
            )
    print("File Organization Complete!")


if __name__ == "__main__":
    main()
