import os
file1=input()
file2=input()
        
try:
    with open(file1 ,"r") as f, open(file2, "w") as to:
        to.write(f.read())
        print(f"copied from {file1} to {file2}")
except FileNotFoundError:
    print(f"file doexnt exist")
except Exception as e:
    print(f" another occured eror:{e}")