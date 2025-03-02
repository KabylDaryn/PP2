import os
filepath = input("path: ")
if os.path.exists(filepath):
    with open(filepath, "r") as f:
        line_count = sum(1 for _ in f)  
    print(f'Count: {line_count}')
else:
    print("file doesn t exist")