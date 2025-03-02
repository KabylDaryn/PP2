import os
def list_contest (path):
    if not os.path.exists(path):
        print("THe path doesn t exist")
        return
    directories=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path ,d))]
    files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path ,f))]
    print("Directories:")
    for directory in directories:
        print(directory)
    print("Files:")
    for file in files:
        print(file)
    print("All:")
    for all in os.listdir(path):
        print(all)

print(list_contest(path=input("path: ")))