class splitting():
    def splitted():
        from Data_transformation import transforming
        from sklearn.model_selection import train_test_split
        df, catdf=transforming.Transform()
        x=df.drop(columns=["Revenue","Name"])
        y=df["Revenue"]
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        return x_train,x_test,y_train,y_test