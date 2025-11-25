from pathlib import Path
import sys
import os

#sys.path.append(str(Path(__file__).resolve().parent))
from API_Caller.API_Caller_Main import main_API_Handler
import API_Caller.API_Variables
from File_Operations.Operations_Main import Convert_JSON_to_EXCEL
import File_Operations.Operations_Variables


def main():
    
    main_API_Handler()
    print(API_Caller.API_Variables.downloaded_JSON_file)
    Convert_JSON_to_EXCEL()


if __name__ =="__main__":
    main()