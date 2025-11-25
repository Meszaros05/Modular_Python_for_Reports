from pathlib import Path
import time
import os
import time
import sys


def Waiter(target_folder: Path, file_pattern: str, timeout: int = 10):
    
    folder=Path(target_folder)
    start_time = time.time()

    while True:
        files = list(folder.glob(file_pattern))
        if (Path(target_folder/file_pattern).exists()):
            # Return the most recently modified file
            latest_file = max(files, key=lambda f: f.stat().st_mtime)
            return True
        if time.time() - start_time > timeout:
                return None  # Timeout reached, no file found

        time.sleep(1)

#targ_fold=Path(r"C:\Program Files\7-Zip")
#target_conv="7z.exe"
#if (Path(targ_fold/target_conv).exists()):
   # file=targ_fold.glob(target_conv)
    #print(list(map(str,file)))
#else: print("sad")

#result=Waiter(targ_fold,target_conv)
#print(result)

#result=Waiter(targ_fold,"tcpdumpasd.pcap")
#print(result)


