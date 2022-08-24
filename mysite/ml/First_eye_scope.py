'''import pandas as pd
import numpy as np
import os.path
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

file = '\eye_trace_scope_data.csv'
file1 = '\eye_trace_on_focus_scope_data.csv'
'''
def get_eye_scope(address,address1,address2) :
    import pandas as pd
    import numpy as np
    import os.path
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    print("Get eye Scope")
    file = '\eye_trace_scope_data.csv'
    file1 = '\eye_trace_on_focus_scope_data.csv'

    if not os.path.exists(address) :
        #print("no %s file" % address)
        exit()
    else :
        #print("exist %s file" % address)

        if not os.path.exists(address1):
            #print("no %s file" % address1)
            exit()
        else:
            #print("exist %s file" % address1)
            address2 = address2+file1
            ###### 112py --> 114py get eye_cord_scope based DBSCAN Clustering
            ###### And 115py


            #get image cord im.read() instead of using DataFrame
            smp = pd.read_csv(address1, sep=',',usecols=[1,2])
            df = pd.read_csv(address, sep=',', usecols=[1,2,3])
            default_label = df.loc[0][2]

            X_train= df[['x_cord','y_cord']]
            X_test = smp[['x_cord','y_cord']]
            Y_train = df['label']
            Y_test = []
            df_dtc = DecisionTreeClassifier()
            df_dtc.fit(X_train,Y_train)
            predition = df_dtc.predict(X_test) #test
            #print(predition[0])

            rows, _ = smp.shape
            eye_trace_on_focus_scope_data = pd.DataFrame(columns=['num', 'x_cord', 'y_cord', 'focus'], dtype=float)

            for i in range(0, rows):
                if predition[i] == default_label:
                    eye_trace_on_focus_scope_data.loc[i] = i, smp.loc[i][0], smp.loc[i][1], 1

                else:
                    eye_trace_on_focus_scope_data.loc[i] = i, smp.loc[i][0], smp.loc[i][1], 2


        eye_trace_on_focus_scope_data.to_csv(address2, index_label=['num'], index=False)
        #print("saved as %s done" %address2)
        print("Done\n")
        return address2
        '''
            if  predition[0] == default_label : ## if image cord is on eye_trace_scope saved as csv named eye_trace_on_focus_scope_data.csv
                if not os.path.exists(address2):
                    print("no file")
                    eye_trace_on_focus_scope_data = pd.DataFrame(columns=['num','x_cord', 'y_cord','focus'], dtype=float)
                    for i in range(0,rows) :
                        eye_trace_on_focus_scope_data.shape.loc[i] = 
                        eye_trace_on_focus_scope_data.loc[rows] = [image rows,x_cord,y_cord,1]
                        eye_trace_scope_data.to_csv('./eye_trace_on_focus_scope_data.csv',index_label = ['num'],index=False)
            
                else:
                    print("exist file")
                    eye_trace_on_focus_scope_data = pd.read_csv(address1, sep=",")
                    rows, _ = eye_trace_on_focus_scope_data.shape
                    # eye_trace_on_focus_scope_data.loc[rows] = [image x_cord,y_cord,1]
                    eye_trace_on_focus_scope_data.to_csv('./eye_trace_on_focus_scope_data.csv')
        
        
                    # 0 is on focus, 1 is on eye_scope, 2 is out of eye_scope
            else :
                if not os.path.exists(address2):
                    eye_trace_on_focus_scope_data = pd.DataFrame(columns=['num', 'x_cord', 'y_cord', 'focus'], dtype=float)
                    print("no file")
        
                    rows, _ = eye_trace_on_focus_scope_data.shape
                    # eye_trace_on_focus_scope_data.loc[rows] = [image rows,x_cord,y_cord,2]
                    eye_trace_scope_data.to_csv('./eye_trace_on_focus_scope_data.csv', index_label=['num'], index=False)
        
                else:
                    print("exist file")
                    eye_trace_on_focus_scope_data = pd.read_csv(address1, sep=",")
                    rows, _ = eye_trace_on_focus_scope_data.shape
                    # eye_trace_on_focus_scope_data.loc[rows] = [image x_cord,y_cord,2]
                    eye_trace_on_focus_scope_data.to_csv('./eye_trace_on_focus_scope_data.csv')
        '''

