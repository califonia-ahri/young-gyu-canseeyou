'''import pandas as pd
#import matplotlib.pyplot as plt
import os.path
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
# based on  scikit-learn DBSCAN Clustering
# using it can make Origin_data frame drop off the trash data
# to make it usefully at least need approximately 100 or more data needed
file = '\eye_cord.csv'
'''
def DBSCAN_Clustering(address) :
    import pandas as pd
    # import matplotlib.pyplot as plt
    import os.path
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler
    # based on  scikit-learn DBSCAN Clustering
    # using it can make Origin_data frame drop off the trash data
    # to make it usefully at least need approximately 100 or more data needed
    print("Start DBSCAN Clustering")
    file = '\eye_cord.csv'

    file1 = address+file
    if not os.path.exists(file1):
        #print("no %s file1" % file1)
        exit()
    else :
        #print("exist file1")
        df = pd.read_csv(file1,usecols=[1,2])
        #print(df)
        df_copy = pd.read_csv(file1, sep=',')
        eye_trace_scope_data = pd.DataFrame( [[0,480,270]],columns = ['num','x_cord' , 'y_cord'],dtype = float)

        data = df[['x_cord', 'y_cord']]

        scaler = StandardScaler()
        df_scale = pd.DataFrame(scaler.fit_transform(df), columns=data.columns)
        model = DBSCAN(eps=0.5, min_samples=5)
        model.fit(df_scale)
        df_scale['cluster'] = model.fit_predict(df_scale)
        #plt.figure(figsize=(8, 8))
        '''for i in range(-1, df_scale['cluster'].max() + 1):
            plt.scatter(df_scale.loc[df_scale['cluster'] == i, 'x_cord'],
                        df_scale.loc[df_scale['cluster'] == i, 'y_cord'],
                        label='eye_tracer ' + str(i)
                        )'''
        #print(df_scale)
        rows,_ = df_scale.shape
        find_default = df_scale.loc[0][2]
        eye_trace_scope_data["label"] = ""
        for i in range(0,rows):
            if df_scale.loc[i][2] == find_default :
                eye_trace_scope_data.loc[i] = i,df_copy.loc[i][1], df_copy.loc[i][2],1
            else :
                eye_trace_scope_data.loc[i] = i,df_copy.loc[i][1], df_copy.loc[i][2],2
        ret_address = address+"\eye_trace_scope_data.csv"
        eye_trace_scope_data.to_csv(ret_address,index_label = ['num'],index=False)
        #print("saved as %s done" %ret_address )
        print("Done\n")
        return ret_address
        '''plt.legend()
        plt.title('eps = 0.5, min_samples = 10', size=15)
        plt.xlabel('x_cord', size=12)
        plt.ylabel('y_cord', size=12)
        plt.show()'''

