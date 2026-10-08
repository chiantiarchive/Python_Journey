


#     pathlib lets you work with file paths using objects instead of plain strings.
#
#     More readable.
#     Works correctly across Windows, macOS, and Linux.
#     Has convenient methods like .read_text(), .write_text(), .exists(), .mkdir().
#     Professional Python code increasingly uses pathlib instead of older os.path style.


from pathlib import Path

# Create a Path object
base_dir = Path(__file__).parent  # directory of this script
output_dir = base_dir / "output"

# Create the folder if it doesn't exist
output_dir.mkdir(exist_ok=True)

# Define a file path
report_path = output_dir / "simple_report.txt"

# Write text using pathlib
report_path.write_text("Hello from pathlib!\n", encoding="utf-8")

# Read text using pathlib
content = report_path.read_text(encoding="utf-8")
print(content)


#   output_dir.mkdir(exist_ok=True) – creates the folder if it doesn’t exist; 
#   exist_ok=True means “don’t error if it already exists.”
#
#   write_text() and read_text() – simple methods that open, read/write, and close the file for you.

#   old style
f = open("sample.txt", "r", encoding="utf-8")
content = f.read()
f.close()

#   Recommended with open(...) style
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

