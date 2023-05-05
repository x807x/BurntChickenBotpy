import json
def change(path:list,data:dict,new:dict):
    print(path,type(path))
    file=str(path[0])
    if(len(path)==1):
        data[file]=new[file]
        return 
    return change(path[1:],data[file],new[file])


class Finance:
    def __init__(self,UserID:int):
        self.id=UserID
        try:
            data=open(f"./data/user/{self.id}.json","r")
        except FileNotFoundError:
            self.file_repair()
        return 
    
    def key_repair(self,path:str):
        path=path.split("/")
        with open(f"./data/user/{self.id}.json","r") as file:
            data=json.load(file)
            file.close()
        new=json.load(open(f"./data/user/1.json","r"))
        print(type(path))
        change(path,data,new)
        print(data,type(data))
        with open(f"./data/user/{self.id}.json","w") as file:
            json.dump(data,file)
            file.close()
        return
        
        
        
    def file_repair(self):
        with open("./data/user/1.json","r") as file:
            data=json.load(file)
            file.close()
        with open(f"./data/user/{self.id}.json","w") as file:
            json.dump(data,file)
            file.close()

    def add(self,nanodollar:int,reason:str,second=False)->bool:
        try:
            with open(f"./data/user/{self.id}.json","r") as file:
                data=json.load(file)
                file.close()
            data["Finance"]["Money"]=data["Finance"]["Money"]+nanodollar
            data["Finance"]["History"].append({"Reason":reason,"Add":nanodollar})
            with open(f"./data/user/{self.id}.json","w") as file:
                json.dump(data,file)
                file.close()
            return True
        except KeyError:
            if(second): return False
            if("Finance" not in data):
                self.key_repair("Finance")
            if("History" not in data["Finance"]):
                self.key_repair("Finance/History")
            if("Mone" not in data["Finance"]):
                self.key_repair("Finance/Money")
            return self.add(nanodollar,reason,second=True)