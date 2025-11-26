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


#----------------------------------------------- JSON
downloaded_JSON_file= None


#----------------------------------------------- JSON