# import urllib library
from urllib.request import Request, urlopen
# import json
import json

API_URL = "http://castellet2526m12.cat/api"

def api_login(app, name, passw):

    req = Request(
        url=f"{API_URL}?a=login&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    response = urlopen(req).read()
    data_json = json.loads(response)
    #print(data_json)
    return data_json["status"] == "success"




def api_register(app, name, passw):
    print(f"{API_URL}?a=register&app={app}&name={name}&pass={passw}")

    req = Request(
        url=f"{API_URL}?a=register&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req).read()
    data_json = json.loads(response)
    return data_json["status"] == "success"




def api_userlist(app):

    req = Request(
        url=f"{API_URL}?a=userlist&app={app}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    print (f"{API_URL}?a=userlist&app={app}")
    response = urlopen(req).read()
    data_json = json.loads(response)
    #print(data_json)
    if data_json["status"] != "success":
        return False
    return data_json["msg"]