import requests
import json,os
from dotenv import load_dotenv
load_dotenv()

app_id=os.getenv("TDXID")
app_key=os.getenv("TDXKey")+"asdf"
auth_url="https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"

class TDXGetter:
    class Auth():
        def __init__(self, app_id, app_key):
            self.app_id = app_id
            self.app_key = app_key

        def get_auth_header(self):
            content_type = 'application/x-www-form-urlencoded'
            grant_type = 'client_credentials'
            return{
                'content-type' : content_type,
                'grant_type' : grant_type,
                'client_id' : self.app_id,
                'client_secret' : self.app_key
            }

    class data():
        def __init__(self, app_id, app_key, auth_response):
            self.app_id = app_id
            self.app_key = app_key
            self.auth_response = auth_response

        def get_data_header(self):
            auth_JSON = json.loads(self.auth_response.text)
            if "error" in auth_JSON:
                print(auth_JSON)
            access_token = auth_JSON.get('access_token')
            return{'authorization': 'Bearer '+access_token}

    def get_data(self,url):
        try:
            a = self.Auth(app_id, app_key)
            auth_response = requests.post(auth_url, a.get_auth_header())
            d = self.data(app_id, app_key, auth_response)
            data_response = requests.get(url, headers=d.get_data_header())
        except:
            print("EXCEPT")
            d = self.data(app_id, app_key, auth_response)
            data_response = requests.get(url, headers=d.get_data_header())    
        return data_response.text
