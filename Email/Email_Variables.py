from pathlib import Path

import os
import sys
import time
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Helper.Help_Functions import *

#################################################
#SMTP Server Config
smtp_server = "mail.hydro.com"
smtp_port =25

#################################################
#Mail config

recipient="gergely.fekete@hydro.com"
#recipients=["gergely.fekete@hydro.com","norbert.nagy.1@hydro.com"]
sender_email = "zabbix_server@hydro.com"
#subject = "CSV Report Attached"
#body = "Hi,\n\nPlease find the attached CSV report.\n\nBest regards,\nPython Script"

################################################

#Files Config (CSV/XLSX))

target_file_convention="Claroty_Sites.xlsx" #==>Add the name of the file that you are looking for, with asterix sign
target_folder=Path(r"C:\Users\a829052\Downloads")   #~Downloads/Claroty/XLSX/ReportType/
#target_file=max(target_folder.glob(target_file_convention), key=lambda f: f.stat().st_mtime)
target_file_PATH=Path(target_folder / target_file_convention)
current_folder=Path(__file__).resolve()
download_folder=Path(r"~Downloads")
xlsx_filename="Claroty_Export"  #name of the attachment



