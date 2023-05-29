from classes.TDXGetter import TDXGetter
import json
import time
DataGetter=TDXGetter()
url_station="https://tdx.transportdata.tw/api/basic/v2/Bike/Station/City/"
url_av="https://tdx.transportdata.tw/api/basic/v2/Bike/Availability/City/"
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

    def clear(self): return self.__init__()

    def __repr__(self)->str:
        return f"{its(self.rentable)} {its(self.returnable)} {self.version} {self.name}"

    def ToStringEn(self)->str:
        return f"{its(self.rentable)} {its(self.returnable)} {self.version} {self.name_en}"

    def station_loads(self,city:str,data:dict):
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
        self.city=city
        return self

    def av_loads(self,data:dict):
        self.rentable=data["AvailableRentBikes"]
        self.returnable=data["AvailableReturnBikes"]
        self.rentable_general=data["AvailableRentBikesDetail"]["GeneralBikes"]
        self.rentable_electric=data["AvailableRentBikesDetail"]["ElectricBikes"]
        return self

    async def Update(self)->str:
        url=f"{url_av}{self.city}?$filter=StationID eq '{self.id}'&$top=1&$format=JSON"
        data=json.loads(DataGetter.get_data(url))
        self.av_loads(data)
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
        url=f"{url_station}{city}?$filter=StationID eq '{id}'&$top=1&$format=JSON"
        data=DataGetter.get_data(url)
        data=json.loads(data)
        self.station_loads(city,data[0])

        url=f"{url_av}{city}?$filter=StationID eq '{self.id}'&$top=1&$format=JSON"
        data=json.loads(DataGetter.get_data(url))
        self.av_loads(data[0])
        self.ERROR=False
        return self


class YouBikeSearcher:
    def __init__(self,limit:int):
        self.limit=limit
    async def updates(self,city:str,data:list):
        this=YouBikeStation()
        this.station_loads(city,data[0])
        
        stations=[]
        stations.append(this)
        url=f"{url_av}{city}?$filter=StationID eq '{this.id}'"
        
        for i in range(1,len(data)):
            this=YouBikeStation()
            this.station_loads(city,data[i])
            stations.append(this)
            url+=f" or StationID eq '{this.id}'"
        url+=f"&$top={len(data)}&$format=JSON"
        start=time.time()
        data=json.loads(DataGetter.get_data(url))
        for i in range(len(data)):
            stations[i].av_loads(data[i])
        return stations
    
    async def name_get(self,city:str,name:str):
        start=time.time()
        try:
            url=f"{url_station}{city}?$filter=contains(StationName/Zh_tw,'{name}')&$top={self.limit+1}&$format=JSON"
            data=json.loads(DataGetter.get_data(url))
        except:
            print("ERROR")
        if(len(data)==0):
            return "找到不到任何相符站點"
        data=await self.updates(city,data)
        string="```py"+table
        for station in data:
            string+=f"{station}\n"
        if(len(data)>self.limit): string+=f"```找到太多站點\n請輸入更詳細的站點名稱"
        else: string+=f"```找到{len(data)}個站點"

        return string
