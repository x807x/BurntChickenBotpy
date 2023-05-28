import json,time
def fix(path:list,data:dict,new:dict):
    print(path,type(path))
    file_name=str(path[0])
    if(len(path)==1):
        for dir in new:
            if(dir not in data):
                data[dir]=new[dir]
    elif(file_name not in data):
        data[file_name]=new[file_name]
        return 
    elif(file_name not in new):
        KeyError
    return fix(path[1:],data[file_name],new[file_name])

def cp(path1:str,path2:str):
    with open(path1,"r",encoding="utf-8") as file:
        with open(path2,"w") as file2:
            file2.write(file.read())


