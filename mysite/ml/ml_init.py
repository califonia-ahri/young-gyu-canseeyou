def first_step(address):
    from .get_eye_cord import get_img,del_img,find_eye_cord
    from .DBSCAN_Clustering import DBSCAN_Clustering

    print("moving your eyes as possible as you can")
    get_img(address)
    find_eye_cord(address)  # get 100 img #return // path + eye_cord.csv
    address_1 = DBSCAN_Clustering(address)  # --> address_1
    # return // path : eye_trace_scope_data.csv
    del_img(address)
    return address_1


def second_step(address,address_1):
    from get_eye_cord import get_img,find_eye_cord,del_img
    from First_eye_scope import get_eye_scope

    print("moving your eyes as possible as you can")
    get_img(address)

    address_2, _ = find_eye_cord(address)  # get 100 img  --> address_2
    address_3 = get_eye_scope(address_1, address_2, address)
    # --> address3
    # return  path : eye_trace_on_focus_scope_data.csv
    del_img(address)
    return address_3


def third_step(address,address_3):
    from get_eye_cord import get_img,find_eye_cord,del_img
    from get_ml_model import eye_scope_model_making

    print("moving your eyes within your focus scope")
    get_img(address)
    address_2, _ = find_eye_cord(address)  # get 100 img  --> address_2
    address_5, address_4 = eye_scope_model_making(address_3, address_2, address)  # --> address5, address4(pkl)
    # return  path : eye_trace_on_focus_scope_data.csv (update) , ml_model
    del_img(address)
    return address_4










