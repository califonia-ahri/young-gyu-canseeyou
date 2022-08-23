def first_step(address):
    from get_eye_cord import *
    from DBSCAN_Clustering import *

    find_eye_cord(address)  # get 100 img #return // path + eye_cord.csv
    address_1 = DBSCAN_Clustering(address)  # --> address_1
    # return // path : eye_trace_scope_data.csv
    del_img(address)
    return address_1


def second_step(address,address_1):
    from get_eye_cord import *
    from First_eye_scope import *

    address_2, _ = find_eye_cord(address)  # get 100 img  --> address_2
    address_3 = get_eye_scope(address_1, address_2, address)
    # --> address3
    # return  path : eye_trace_on_focus_scope_data.csv
    del_img(address)
    return address_3


def third_step(address,address_3):
    from get_eye_cord import *
    from get_ml_model import *

    address_2, _ = find_eye_cord(address)  # get 100 img  --> address_2
    address_5, address_4 = eye_scope_model_making(address_3, address_2, address)  # --> address5, address4(pkl)
    # return  path : eye_trace_on_focus_scope_data.csv (update) , ml_model
    del_img(address)
    return address_4










