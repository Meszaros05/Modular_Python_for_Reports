import requests
import os
import sys
import time
import pandas as pd
import urllib3
from datetime import datetime
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Helper.Help_Functions import *

#WARNING!!! Be aware that variables - API_PATH,  Licenses_API_Site_Code and filename should be set up manually.

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#############################################
#API type
Sites_API="/ranger/sites"                               #Sites export
Licenses_API_Site_Code="21"                                                               #configured manually (ID of the site)
Licenses_API="/ranger/license/"+Licenses_API_Site_Code  #Licenses export

API_PATH=Sites_API                                                                            #Configured manually (Sites_API, Licenses_API, etc)
#############################################
#API user/call variables
SERVER = "clarotyemc.nhy.hydro.com"
USER = "API_admin"
PASSWORD = "Admin123!"
VERIFY_SSL = False

#############################################
#API request config.
filename_Sites="sites_claroty"
filename_Licenses="licenses_claroty"
#############################################
#Token
token=None

#############################################
#files config


current_file=Path(__file__).resolve()
target_folder=Path(r"~/Downloads/Claroty_Sites_Reports")                                                 #target_folder=Path(r"C:\Users\a829052\Downloads") 
#target_folder=Path(r"~/Downloads/Claroty_Licenses_Reports")     
filename=f"{filename_Sites}.json"                                                   #should be substituted the filename of the reported topic 
download_folder=Path(r"~Downloads")
#abs_path_target_file=os.path.join(target_folder,filename)
abs_path_target_file=target_folder/filename


               



