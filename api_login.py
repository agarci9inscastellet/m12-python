# import urllib library
from urllib.request import Request, urlopen
# import json
import json

def api_login(app, name, passw):

    req = Request(
        url=f"http://www.castelletm12b.cat/api.php?a=login&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req).read()
    data_json = json.loads(response)
    return data_json["login"]




def api_register(app, name, passw):

    req = Request(
        url=f"http://www.castelletm12b.cat/api.php?a=register&app={app}&name={name}&pass={passw}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req).read()
    data_json = json.loads(response)
    return data_json["success"]




def api_userlist(app):

    req = Request(
        url=f"http://www.castelletm12b.cat/api.php?a=userlist&app={app}", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req).read()
    data_json = json.loads(response)
    return data_json["msg"]