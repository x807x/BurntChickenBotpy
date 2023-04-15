import  json, ssl, urllib.request, asyncio

url_tp = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
url_ty="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url_hc="https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
url_tc="https://datacenter.taichung.gov.tw/swagger/OpenData/9af00e84-473a-4f3d-99be-b875d8e86256"
url_nt_1="https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/json?size=5000"
url_nt_2="https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=10000"
context = ssl._create_unverified_context()
table="""
剩餘YouBike
  | 剩餘空車架
  |   | 站點名稱
"""

def its(n:int)->str:
    s=str(n)
    s=" "*(3-len(s))+s
    return s

def ToString(station:dir)->str:
    bikes=int(station["sbi"])
    empty=int(station["tot"])-bikes
    if(station["sna"].startswith("YouBike2.0_")):
        name=station["sna"][11:]
    else: name=station["sna"]
    return f"{its(bikes)} {its(empty)} {name}"

def output(data):
    if(data==[]): return "沒找到任何YouBike站"
    if(type(data)==dict):
        return "```"+table+ToString(data)+"```"
    if(type(data)==list):
        print("list data")
        string="```"+table
        for station in data:
            string+=ToString(station)+"\n"
        string+="```"+f"找到{len(data)}個站點"
        if(len(string)>1000): return f"找到{len(data)}個站點\n請輸入更詳細的站名"
        return string
    print("ERROR")
    ValueError

async def get_station(data:list,id:int):
    station=None
    for i in data:
        if(id==int(i["sno"])):
            station=i
    return station

async def get_station2(data:list,id:int):
    l=0;r=len(data)
    station=None
    while r-l>=1:
        mid=(l+r)//2
        temp=int(data[mid]["sno"])
        if(temp==id):
            station=data[mid]
            break
        elif(id<temp): r=mid
        else: l=mid
        if(r-l==1 and id!=temp):
            break
    return station

async def get_station_tp(id:int):
    with urllib.request.urlopen(url_tp, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    return await get_station2(data,id)

async def get_station_nt_1(id:int):
    with urllib.request.urlopen(url_nt_1, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    return await get_station2(data,id)


async def get_station_nt_2(id:int):
    with urllib.request.urlopen(url_nt_2, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    return await get_station2(data,id)

async def get_station_ty(id:int):
    with urllib.request.urlopen(url_ty, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    data=data["retVal"]
    try: return data[str(id)]
    except KeyError: return None

async def get_station_hc(id:int):
    with urllib.request.urlopen(url_hc, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    return await get_station(data["retVal"],id)

async def get_station_tc(id:int):
    with urllib.request.urlopen(url_tc, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    return await get_station(data["retVal"],id)

async def search_stations_tp(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_tp, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    for i in data:
        temp=i["sna"]
        if(content in temp):
            stations.append(i)
    print("search tp finished")
    return stations

async def search_stations_nt_1(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_nt_1,context=context) as jsondata:
        data=json.loads(jsondata.read().decode("utf-8"))
        jsondata.close()
    for i in data:
        temp=i["sna"]
        if(content in temp):
            stations.append(i)
    print("search nt_1 finished")
    
    return stations

async def search_stations_nt_2(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_nt_2,context=context) as jsondata:
        data=json.loads(jsondata.read().decode("utf-8"))
        jsondata.close()
    for i in data:
        temp=i["sna"]
        if(content in temp):
            stations.append(i)
    print("search nt_2 finished")
    return stations

async def search_stations_tc(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_tc, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    data=data["retVal"]
    for i in data:
        temp=i["sna"]
        if(content in temp):
            stations.append(i)
    print("search tc finished")
    return stations


async def search_stations_ty(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_ty, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    data=data["retVal"]
    for i in data:
        temp=data[i]["sna"]
        if(content in temp):
            stations.append(data[i])
    print("search ty finished")
    return stations

async def search_stations_hc(content:str)->list:
    stations=[]
    with urllib.request.urlopen(url_hc, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    data=data["retVal"]
    for i in data:
        temp=i["sna"]
        if(content in temp):
            stations.append(i)
    print("search hc finished")
    return stations

async def find(id_name)->str:
    if(id_name.isdigit()):
        station_id=int(id_name)
        station=await asyncio.gather(get_station_tp(station_id),
                                    get_station_nt_1(station_id),
                                    get_station_nt_2(station_id),
                                    get_station_ty(station_id),
                                    get_station_hc(station_id),
                                    get_station_tc(station_id))
        for i in station:
            if(type(i)==dict):
                return output(i)
    else:
        station_name=id_name
        stations=[]
        parrel=await asyncio.gather(search_stations_tp(station_name),
                            search_stations_ty(station_name),
                            search_stations_tc(station_name),
                            search_stations_hc(station_name),
                            search_stations_nt_1(station_name),
                            search_stations_nt_2(station_name))
        for data in parrel: stations+=data
        try:
            return (output(stations))
        except: print("ERROR")

