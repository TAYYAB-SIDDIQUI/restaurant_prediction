class Selecting():
    def select():
        import pandas as pd
        import numpy as np
        from sklearn.linear_model import Lasso,Ridge,LinearRegression
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.ensemble import RandomForestRegressor
        from Data_splitting import splitting
        from sklearn.metrics import mean_squared_error,precision_score
        from sklearn.preprocessing import MinMaxScaler
        norm=MinMaxScaler()
        global x_train,x_test,y_train,y_test
        x_train,x_test,y_train,y_test=splitting.splitted()
        models=[Lasso,Ridge,LinearRegression,DecisionTreeRegressor,RandomForestRegressor]
        rmse_values=[]
        precision_value=[]
        score_values=[]
        for i in models:
            if i==RandomForestRegressor:
                model=i(n_estimators=100,random_state=42)
                model.fit(x_train,y_train)
                pass
            else:
                model=i()
                model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            rmse_values.append(np.sqrt(mean_squared_error(y_test,y_pred)))
            score_values.append(model.score(x_test,y_test))   
        model_df=pd.DataFrame({"model":models,"rmse":rmse_values,"score":score_values})
        final_model=model_df[(model_df["score"]==max(model_df["score"]))]
        print(final_model)
        return final_model
