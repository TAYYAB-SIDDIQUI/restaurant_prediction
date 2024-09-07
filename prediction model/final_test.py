def run():
    from Data_ingestion import ingestion
    from Data_preprocessing import processing
    from feature_engineering import features
    from Data_transformation import transforming
    from Data_splitting import splitting
    from model_selection import Selecting
    from model_train import training
   # ingestion.file()
   # processing.process()
   # features.featurefunc()
   # transforming.Transform()
   # splitting.splitted()
   # Selecting.select()
    training.train()
run()