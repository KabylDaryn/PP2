import os 
def list_to_file(fpath , list):
    with open(fpath ,"w") as f:
        for l in list:
            f.write(l +"/n")
file=input("Path: ")
my_list=input().split()
print(list_to_file(file,my_list))