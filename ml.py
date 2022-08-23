def get_ml_path(address):
    from ml_init import *

    address_1 = first_step(address) ### 100 img needed & del it
    address_3 = second_step(address,address_1) ### 100 img needed & del it
    address_4 = third_step(address,address_3) ### 100 img needed & del it

    return address_4

def get_focus_int_by_ml(address,address_4):
    import joblib
    import numpy as np

    from get_eye_cord import *
    from ml_init import *

    #address is user dir path && need file
    # //shape_predictor_68_face_landmarks.dat &&//haarcascade_eye_tree_eyeglasses.xml


    ml_model = joblib.load(address_4)

    _, X_test = find_eye_cord(address) ## 1 img needed & del it
    X_test = np.reshape(X_test, (1, 2))
    predition = ml_model.predict(X_test)
    result = int(predition[0])
    return result # 0 or 1 or 2 return
