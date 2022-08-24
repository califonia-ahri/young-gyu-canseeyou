import joblib
import numpy as np
from .get_eye_cord import find_eye_cord
from .ml_init import first_step,second_step,third_step

def get_ml_path(address):
    print("##################################")
    print("Start Machine Learning First Step")
    print("##################################")
    address_1 = first_step(address) ### 100 img needed & del it
    print("First Step Done\n")

    print("##################################")
    print("Start Machine Learning Second Step")
    print("##################################")
    address_3 = second_step(address,address_1) ### 100 img needed & del it
    print("Second Step Done\n")

    print("##################################")
    print("Start Machine Learning Third Step")
    print("##################################")
    address_4 = third_step(address,address_3) ### 100 img needed & del it
    print("Third Step Done\n")
    print("Making Machine Learning Model %s" %address_4)
    return address_4

def get_focus_int_by_ml(address,address_4):

    #address is user dir path && need file
    # //shape_predictor_68_face_landmarks.dat &&//haarcascade_eye_tree_eyeglasses.xml

    ml_model = joblib.load(address_4)

    print("\n\n#############")
    print("Get eye cord by periodic 5 sec img")
    _, X_test = find_eye_cord(address) ## 1 img needed & del it
    X_test = np.reshape(X_test, (1, 2))
    predition = ml_model.predict(X_test)
    print("#############")
    print("\n\n")
    result = int(predition[0])
    return result # 0 or 1 or 2 return
