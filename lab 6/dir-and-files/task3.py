import os
def exist(path):
    if os.path.exists(path):
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("The path doesn t exist")
    return

print(exist(path=input("path: ")))