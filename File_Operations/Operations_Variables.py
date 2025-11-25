from pathlib import Path
import os
import sys
import time
sys.path.append(str(Path(__file__).resolve().parent.parent))
import API_Caller.API_Variables as API_var

import Email.Email_Variables as Email_var




################################################
#JSON file ()
current_file=Path(__file__).resolve()
target_JSON_folder=API_var.target_folder    #=Path(r"C:\Users\a829052\Downloads")   #~Downloads/Claroty/XLSX/ReportType/         #JSON folder
target_JSON_file_PATH=API_var.abs_path_target_file    #JSONfile abs PATH
target_JSON_file=API_var.filename
download_folder=Path(r"~Downloads")

#!!!!!!!!!!!!!!!!!!!!!!!
downloaded_JSON_file=API_var.downloaded_JSON_file


################################################
#Excel file ()
target_CSV_folder=Email_var.target_folder
#target_CSV_file=Email_var.target_file
target_CSV_file_PATH = Email_var.target_file_PATH
target_file_convention=Email_var.target_file_convention


################################################
#Excel name convention
CSV_Claroty_Sites=API_var.filename_Sites
CSV_Claroty_Licenses=API_var.filename_Licenses