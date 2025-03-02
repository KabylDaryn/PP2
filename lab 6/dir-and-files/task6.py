import os
import string

os.makedirs("Alphabetf", exist_ok=True)
for letter in string.ascii_uppercase:
    with open(os.path.join("Alphabetf", f"{letter}.txt"), "w") as file:
        file.write(f"This is file {letter}.txt")
