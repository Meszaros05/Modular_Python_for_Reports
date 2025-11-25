import json
import pandas as pd
import openpyxl
import os 
from pathlib import Path
import time
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Helper.Help_Functions import Waiter as help_waiter
import File_Operations.Operations_Variables as var
from API_Caller.API_Variables import downloaded_JSON_file as API_var



def Convert_JSON_to_EXCEL ():
    
    
    print(var.downloaded_JSON_file)
    # Check if the variable contains data
    if  var.downloaded_JSON_file is not None:
        # Load JSON data from variable
        data = var.downloaded_JSON_file

        # Extract the "objects" key
        record = data.get("objects", [])

        # Convert JSON data to pandas DataFrame
        df = pd.json_normalize(record)

        # Remove old file if exists
        if os.path.exists(var.target_CSV_file_PATH):
            os.remove(var.target_CSV_file_PATH)
        # Save to Excel
        df.to_excel(var.target_CSV_file_PATH, index=False)
        print(f"Excel file created: {var.target_file_convention}")
    else:
        print("JSON data is not available in API_var.downloaded_JSON_file")

    


