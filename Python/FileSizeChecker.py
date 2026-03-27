# import os

# file = "TestFile.txt"
# file_size = os.path.getsize(file)

# print(file_size)

## More modern and software friendly approach:

from pathlib import Path

file_path = Path("TestFile.txt")

try:
    file_size = file_path.stat().st_size
    print(file_size)
except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")