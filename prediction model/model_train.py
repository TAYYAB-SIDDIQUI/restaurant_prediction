class training():
    def train():
        from Data_splitting import splitting
        import numpy as np
        from sklearn.metrics import mean_squared_error
        from sklearn.preprocessing import MinMaxScaler
        x_train,x_test,y_train,y_test=splitting.splitted()
        from sklearn.ensemble import RandomForestRegressor
        model=RandomForestRegressor(n_estimators=100,random_state=42)
        norm=MinMaxScaler()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        score=model.score(x_test,y_test)
        rmse=np.sqrt(mean_squared_error(y_test,y_pred))
        from Data_ingestion import ingestion
        df=ingestion.file()
        percentage_error=(rmse/df["Revenue"].mean())*100
        import joblib
        modelsave=joblib.dump(model,"restaurantprediction.pkl")
        print(model,rmse,score,percentage_error)
        return modelsave
    def infoofmodel():
        modelname="RandomForestRegressor(random_state=42)"
        accuracy="99.92%"
        mserror="7466.05%"
        percent_mserror="1.14%"
        return modelname,accuracy,mserror,percent_mserror