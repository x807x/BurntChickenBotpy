from classes.TDXGetter import TDXGetter
import json
DataGetter=TDXGetter()

table="""
剩餘YouBike
  | 剩餘空車架
  |   | 版本
  |   | | 站點名稱
"""

def its(n:int)->str:
    s=str(n)
    s=" "*(3-len(s))+s
    return s

class YouBikeStation:
    def __init__(self):
        self.city=""
        self.name=""
        self.name_en=""
        self.id=0
        self.version=0
        self.rentable=0
        self.rentable_general=0
        self.rentable_electric=0
        self.returnable=0
        self.capacity=0
        self.longitude=0
        self.latitude=0
        self.ERROR=True
        return None

    def __repr__(self)->str:
        return f"{its(self.rentable)} {its(self.returnable)} {self.version} {self.name}"

    def ToStringEn(self)->str:
        return f"{its(self.rentable)} {its(self.returnable)} {self.version} {self.name_en}"

    async def Update(self)->str:
        url=f"https://tdx.transportdata.tw/api/basic/v2/Bike/Availability/City/{self.city}?%24filter=contains%28StationID%2C%27{self.id}%27%29&%24orderby=StationID&%24top=20&%24format=JSON"
        data=json.loads(DataGetter.get_data(url))
        self.rentable=data["AvailableRentBikes"]
        self.returnable=data["AvailableReturnBikes"]
        self.rentable_general=data["AvailableRentBikesDetail"]["General"]
        self.rentable_electric=data["AvailableRentBikesDetail"]["ElectricBikes"]

        return self

    async def find(self,city:str,id:int):
        self.city=""
        self.name=""
        self.name_en=""
        self.id=0
        self.version=0
        self.rentable=0
        self.rentable_general=0
        self.rentable_electric=0
        self.returnable=0
        self.capacity=0
        self.longitude=0
        self.latitude=0
        self.ERROR=True
        if(city=="" or id==0): return None
        url=f"https://tdx.transportdata.tw/api/basic/v2/Bike/Station/City/{city}?%24filter=contains%28StationID%2C%27{id}%27%29&%24orderby=StationID&%24top=30&%24format=JSON"
        data=DataGetter.get_data(url)
        data=json.loads(data)
        if(len(data)>1):
            l=0;r=len(data)
            if(int(data[0]["StationID"])<id):
                data=[]
            
        if(len(data)==1):
            data=data[0]
            self.version=data["ServiceType"]
            self.id=data["StationID"]
            temp=data["StationName"]["Zh_tw"]
            if(temp.startswith(f"YouBike{self.version}.0_") and temp[10]=='_'): temp=temp[11:]
            self.name=temp
            temp=data["StationName"]["En"]
            if(temp.startswith(f"YouBike{self.version}.0_") and temp[10]=='_'): temp=temp[11:]
            self.name_en=temp
            self.capacity=data["BikesCapacity"]
            self.longitude=data["StationPosition"]["PositionLon"]
            self.latitude=data["StationPosition"]["PositionLat"]

        url=f"https://tdx.transportdata.tw/api/basic/v2/Bike/Availability/City/{city}?%24filter=contains%28StationID%2C%27{id}%27%29&%24orderby=StationID&%24top=20&%24format=JSON"
        data=json.loads(DataGetter.get_data(url))
        data=data[0]
        self.city=city
        self.id=data["StationID"]
        self.rentable=data["AvailableRentBikes"]
        self.returnable=data["AvailableReturnBikes"]
        self.rentable_general=data["AvailableRentBikesDetail"]["GeneralBikes"]
        self.rentable_electric=data["AvailableRentBikesDetail"]["ElectricBikes"]
        
        return self


class YouBikeSearcher:
    async def name_get(self,city:str,name:str):
        try:
            url=f"https://tdx.transportdata.tw/api/basic/v2/Bike/Station/City/{city}?%24select=StationID&%24filter=contains%28StationName%2FZh_tw%2C%27{name}%27%29&%24top=10000&%24format=JSON"
            data=json.loads(DataGetter.get_data(url))
        except:
            print("ERROR")
        if(len(data)>30):
            return f"找到{len(data)}個站點\n需要更詳細的名稱"
        string="```py\n"+table
        temp=YouBikeStation()
        for station in data:
            await temp.find(city,station["StationID"])
            string+=f"{temp}\n"
        string+=f"```\n找到{len(data)}個站點"
        return string
