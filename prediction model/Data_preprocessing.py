class processing():
    def process():
        from Data_ingestion import ingestion
        import pandas as Pd 
        import numpy as np
        df=ingestion.file()
        null_percentages=np.array((df.isnull().sum())*100/len(df))
        null_names=np.array(df.isnull().sum().keys())
        for i in range(len(null_percentages)):
            if null_percentages[i]>17:
                df=df.drop(columns=[null_names[i]])
        duplicates=list(df.duplicated())
        for i in duplicates:
            if i==True:
                df.drop_duplicates(inplace=True)
        return df
    