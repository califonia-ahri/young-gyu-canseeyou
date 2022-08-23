
def eye_scope_model_making(address,address1,address2) :

    import pandas as pd
    import numpy as np
    import os.path
    import joblib
    from sklearn.tree import DecisionTreeClassifier

    file = '\eye_trace_on_focus_scope_data.csv'

    if not os.path.isfile(address) :
        print("no %s file" % address)
        exit()
    else :
        print("exist %s file" % address)
        if not os.path.isfile(address1):
            print("no %s file" % address1)
            exit()
        else:
            print("exist %s file" %address1)
            #get image cord im.read() instead of using DataFrame
            smp = pd.read_csv(address1, sep=',', usecols=[1, 2])
            df = pd.read_csv(address, sep=',', usecols=[1, 2, 3])

            default_label = df.loc[0][2]

            X_train = df[['x_cord', 'y_cord']]
            X_test = smp[['x_cord', 'y_cord']]
            Y_train = df['focus']
            Y_test = []
            df_dtc = DecisionTreeClassifier()
            df_dtc.fit(X_train, Y_train)
            predition = df_dtc.predict(X_test)  # test
            # print(predition[0])
            rows, _ = smp.shape

            eye_trace_on_focus_scope_data = pd.DataFrame(columns=['x_cord', 'y_cord', 'focus'], dtype=float)
            for i in range(0, rows):
                if predition[i] == default_label:
                    eye_trace_on_focus_scope_data.loc[i] = smp.loc[i][0], smp.loc[i][1], 0
                else:
                    eye_trace_on_focus_scope_data.loc[i] =  smp.loc[i][0], smp.loc[i][1], 1

            print(address2)
            result_df = pd.concat([df[['x_cord', 'y_cord','focus']],eye_trace_on_focus_scope_data],sort=False)

            print(result_df)
            result_df.to_csv(address, index=False)


            address3 = address2+"\ml_model.pkl"
            joblib.dump(df_dtc,address3)
        print("Data saved as %s done" %address)
        print("Model saved as %s done" %address3)
        return address2,address3
