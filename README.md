# File Organizer

A Python-based utility that automatically organizes files in your Downloads folder based on file types and document patterns.

## Features

- Automatically organizes files from your Downloads folder
- Supports custom file extension mappings
- Handles document type-based organization
- Creates destination folders automatically
- Non-destructive operation (moves files instead of deleting)

## Setup

1. Clone this repository:

```bash
git clone git@github.com:ermand/file_organizer.git
cd file_organizer
```

2. Ensure you have Python installed on your system (Python 3.x recommended)

3. The project uses only Python standard library modules, so no additional dependencies are required.

## Configuration

The project uses two CSV files for configuration:

```bash
cp sample_document_mappings.csv document_mappings.csv
cp sample_extension_mappings.csv extension_mappings.csv
```

### extension_mappings.csv

- Maps file extensions to destination folders
- Format: `extension,folder`
- Example:

  ```csv
  .pdf,Documents
  .odt,Documents
  .csv,Documents
  .jpg,Images
  .jpeg,Images
  ```

### document_mappings.csv

- Maps document patterns to specific folders
- Format: `pattern,destination`
- Example:

  ```csv
  invoice,Documents/Invoices
  flight,Documents/Flight
  ```

## Usage

Simply run the main script:

```bash
python main.py
# or
python3 main.py
```

The script will:

1. Scan your Downloads folder
2. Identify files based on extensions and patterns
3. Move them to appropriate folders within Downloads
4. Create destination folders if they don't exist

## How It Works

1. The script first loads configuration from both CSV files
2. It then scans the Downloads directory for files
3. For each file:
   - Checks if the extension is in the configured mappings
   - If matched, checks for document type patterns
   - Moves the file to the appropriate folder

## Notes

- The script runs on your `Downloads` folder by default
- Files are moved, not copied
- Existing files in destination folders won't be overwritten
- The script will create destination folders if they don't exist

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
