import requests
import pandas as pd
import urllib3
import sys
from datetime import datetime
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import Helper.Help_Functions as help_waiter
import API_Caller.API_Variables as var

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_token():
    response = requests.post(
        f"https://{var.SERVER}/auth/authenticate",
        json={"username": var.USER, "password": var.PASSWORD},
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"},
        verify=var.VERIFY_SSL

    )
    
    data = response.json()
    return data.get("token")  #==> need to be called


#This function is able to download JSON formatted files via API
def fetch_sites(token):
    response=requests.get(
        f"https://{var.SERVER}{var.API_PATH}",
        headers={
            "Authorization": var.token,
            "Accept":"Application/json"
            },
        params={"page": 1, "per_page": 100},
        verify=var.VERIFY_SSL,
        
    )
    

    with open(var.abs_path_target_file,"w",encoding="utf-8") as f:
        f.write(response.text)
    response.raise_for_status()
    return response.json()

var.downloaded_JSON_file
def main_API_Handler():
    var.token = get_token()
    print(var.token)
    var.downloaded_JSON_file=fetch_sites(var.token)




    


