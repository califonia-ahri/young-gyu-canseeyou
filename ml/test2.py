
import sys
import os
from ml import *

if(len(sys.argv) > 2):
    print("plz input 1 path_address")
    exit()
else:
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()

    address = sys.argv[1]
    address_1 = address+"\ml_model.pkl"
    if not os.path.exists(address_1):
        print("no ml file")
        print("Init")
        address_1 = get_ml_path(address)
    else :
        print("exist ml file")
    result = get_focus_int_by_ml(address,address_1)
    print("eye_focus_predition_by_Ml_model : %d" %result)
