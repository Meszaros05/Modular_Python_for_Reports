from pathlib import Path
import sys
import os

#sys.path.append(str(Path(__file__).resolve().parent))
from API_Caller.API_Caller_Main import main_API_Handler
from File_Operations.Operations_Main import Convert_JSON_to_EXCEL
from Email.Email_Main import Email


def main():
    
    main_API_Handler()
    Convert_JSON_to_EXCEL()
    Email()

if __name__ =="__main__":
    main()
    
