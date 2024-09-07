class transforming():
    def Transform():
        from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
        from feature_engineering import features
        import numpy as np
        import pandas as pd
        global df
        df=features.featurefunc()
        global cat_var
        global num_var
        num_var=[features for features in df.columns if df[features].dtype!="O"]
        cat_var=[features for features in df.columns if df[features].dtype=="O"]
        encoder=OrdinalEncoder()
        norm=MinMaxScaler()
        global cat_df
        cat_df=pd.DataFrame()
        for i in cat_var:
            cat_df[i]=df[i]
            df[i]=encoder.fit_transform(np.array(df[i]).reshape(-1,1))
        return df,cat_df
    def dic_map():
        from feature_engineering import features
        df=features.featurefunc()
        ndf,cat_df=transforming.Transform()
        cat_var=[features for features in df.columns if df[features].dtype=="O"]
        dic=[]
        for col in cat_var:
            dic.append({})
            for i,j in zip(cat_df[col],ndf[col]):
                for h in range(len(dic)):
                    dic[-1].update({i:j})
        res_name_dic,location_dict,Cuisine_dic,park_dict=dic[0],dic[1],dic[2],dic[3]
        #print("\ndictionaries:restaurant,locaion,Cuisine,parking_availability\nname        :res_name_dic,location_dict,Cuisine_dic,park_dict\n")           
        return res_name_dic,location_dict,Cuisine_dic,park_dict
transforming.dic_map()
        