# import urllib library
from urllib.request import Request, urlopen
# import json
import json
from urllib.parse import quote

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

def api_getpunts(app, name, passw):

    req = Request(
        url=f"{API_URL}?a=login&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    response = urlopen(req).read()
    data_json = json.loads(response)
    #print(data_json)
    if data_json["status"] == "success":
        return data_json['user']["punts"]
    else:
        return False



def api_updatepunts(app, name, passw, punts):
    """Send punts (points) to the API for the given user/app.

    Returns True if the API responds with status == 'success', otherwise False.
    """
    # Quote all parameters to be safe
    req = Request(
        url=(f"{API_URL}?a=updatepunts&app={quote(app)}&name={quote(name)}"
             f"&pass={quote(passw)}&punts={quote(str(punts))}"),
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        response = urlopen(req).read()
        data_json = json.loads(response)
        return data_json.get("status") == "success"
    except Exception:
        return False


def api_register(app, name, passw):
    #print(f"{API_URL}?a=register&app={app}&name={name}&pass={passw}")

    req = Request(
        url=f"{API_URL}?a=register&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req).read()
    data_json = json.loads(response)
    return data_json["status"] == "success"

def api_deleteuser(app, username, password):
    # Build request URL (quote parameters to be safe)
    req = Request(
        url=f"{API_URL}?a=deleteuser&app={app}&name={username}&pass={password}",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        response = urlopen(req).read()
        data_json = json.loads(response)
        return data_json.get("status") == "success"
    except Exception:
        # On any error (network, JSON parsing, etc.) return False
        return False


def api_userlist(app):

    req = Request(
        url=f"{API_URL}?a=userlist&app={app}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    #print (f"{API_URL}?a=userlist&app={app}")
    response = urlopen(req).read()
    data_json = json.loads(response)
    #print(data_json)
    if data_json["status"] != "success":
        return False
    return data_json["msg"]

