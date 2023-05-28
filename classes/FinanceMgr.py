import json,time
from functions.Writer import fix
class FinanceMgr:
    def __init__(self,UserID:int):
        self.id=UserID
        path=f"./data/user/{self.id}.json"
        try:
            with open(path,"r") as file:
                data=json.load(file)
                file.close()
            data["UserID"]=self.id
            with open(path,"w") as file:
                json.dump(data,file)
                file.close()
        except FileNotFoundError:
            self.file_repair()
        return 

    def key_repair(self,path:str):
        path=path.split("/")
        with open(f"./data/user/{self.id}.json","r") as file:
            data=json.load(file)
            file.close()
        new=json.load(open(f"./data/user/1.json","r"))
        fix(path,data,new)
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
            data["Finance"]["History"].append({"Reason":reason,"Add":nanodollar,"Time":time.time_ns()})
            with open(f"./data/user/{self.id}.json","w") as file:
                json.dump(data,file)
                file.close()
            return True
        except KeyError:
            if(second): return False
            self.key_repair("Finance")
            return self.add(nanodollar,reason,second=True)

    def minus(self,nanodollar:int,reason:str,second:bool=False):
        try:
            with open(f"./data/user/{self.id}.json","r") as file:
                data=json.load(file)
                file.close()
            data["Finance"]["Money"]=data["Finance"]["Money"]-nanodollar
            data["Finance"]["History"].append({"Reason":reason,"Minus":nanodollar,"Time":time.time_ns()})
            with open(f"./data/user/{self.id}.json","w") as file:
                json.dump(data,file)
                file.close()
            return True
        except KeyError:
            if(second==True): return False
            self.key_repair("Finance")
            return self.minus(nanodollar,reason,True)

    def money(self,second=False)->int:
        with open(f"./data/user/{self.id}.json","r") as file:
            data=json.load(file)
            file.close()
        try: return data["Finance"]["Money"]
        except KeyError:
            if(second): return False
            self.key_repair("Finance/Money")
            return self.second(second=True)