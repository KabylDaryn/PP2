import os
filepath=input()
if os.path.exists(filepath) and os.access(filepath ,os.W_OK):
    os.remove(filepath)
else:
    print("Not found")