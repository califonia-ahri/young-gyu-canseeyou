
import sys
import os


def starting():
    from .mll import get_ml_path, get_focus_int_by_ml
    if(len(sys.argv) > 2):
        print("plz input 1 path_address")
        exit()
    else:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

        address = "C:\\apis\\photo"
        address_1 = address+"\ml_model.pkl"
        if not os.path.exists(address_1):
            print("no ml file")
            print("Init")
            address_1 = get_ml_path(address)
        else :
            print("exist ml file")
            if not os.path.exists(address+"\\*.PNG") :
                get_img_per_5s(address)
        result = get_focus_int_by_ml(address,address_1)
        print("eye_focus_predition_by_Ml_model : %d" %result)
        
    if __name__=="__main__":
        print("asdfasdfasdf")
        starting()
