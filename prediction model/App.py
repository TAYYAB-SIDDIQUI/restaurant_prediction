from flask import Flask,render_template,request,redirect,url_for
import os
import numpy as np
import pandas as pd
import platform
app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="uploads"

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")
@app.route("/action/<action_name>")
def start(action_name):
    if action_name=="startpage":
        num=1
        from feature_engineering import features
        df=features.featurefunc()
        path="Data/restaurant_data.csv"
        absolute_path=os.path.abspath(path)
        if num==1:
            os.path.exists(absolute_path)
            os.system(absolute_path)
    return render_template("index.html")
@app.route("/<action_name2>")
def viewmodel_(action_name2):
    if action_name2=="viewmodel":
        from model_train import training
        model,score,rmse,percent_error=training.infoofmodel()
        return f"<body style='background-color:rgb(31,3,49);'><h1 style='color:white;'>model name : {model} <br><br> score : {score}<br><br> percentage of avg error : {percent_error}</h1>"
    return "Done"
@app.route("/adddata",methods=["GET","POST"])
def add():
    return render_template("adddata.html")
@app.route("/adddata/data",methods=["GET","POST"])
def data():
    if request.method=="POST":
        location=request.form.get("Location")
        cuisine=request.form.get("cuisine")
        Rating=request.form.get("Rating")
        Seating_Capacity=request.form.get("Seating")
        Amp=request.form.get("Average Meal Price")
        mb=request.form.get("Marketing Budget")
        Smf=request.form.get("Social Media Followers")
        ce=request.form.get("Chef Experience Years")
        nor=request.form.get("Number of Reviews")
        arl=request.form.get("Avg Review Length")
        As=request.form.get("Ambience Score")
        sqs=request.form.get("Service Quality Score")
        pa=request.form.get("Parking Availability")
        wr=request.form.get("Weekend Reservations")
        wkr=request.form.get("Weekday Reservations")
        global form_df
        form_df=pd.DataFrame({"Location":[location],
                              "cuisone":[cuisine],
                              "rating":[Rating],
                              "Seating":[Seating_Capacity],
                              "Amp":[Amp],
                              "mb":[mb],
                              "Smf":[Smf],
                              "Ce":[ce],
                              "nor":[nor],
                              "arl":[arl],
                              "As":[As],
                              "sqs":[sqs],
                              "pa":[pa],
                              "wr":[wr],
                              "wkr":[wkr]})
        return render_template("adddata.html"),"""<p>comp</p>"""
    return render_template("adddata.html"),form_df
def allow(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
@app.route("/File",methods=["GET","POST"])
def file():
    if request.method=="POST":
        file=request.files.get("file")
        if file and file.filename:
            file.save(f"{app.config['UPLOAD_FOLDER']}/{file.filename}")
        else:
            print("no file import")
            return f"file loaded {file.filename}"
    return "file"
@app.route("/analyze",methods=["GET","POST"])
def analyse():
    if request.method=="GET":
        filtered_data1=[]
        a,b=data()
        datas=b
        from Data_transformation import transforming
        res_name_dic,location_dict,Cuisine_dic,park_dict=transforming.dic_map()
        ind=[0,1,2,13]
        dictionaries=[res_name_dic,location_dict,Cuisine_dic,park_dict]
        datas["Location"]=datas["Location"].map(location_dict)
        datas["cuisone"]=datas["cuisone"].map(Cuisine_dic)
        datas["pa"]=datas["pa"].map(park_dict)
        print(datas)
        filtered_datas=[]
        for i in datas.iloc[0]:
            element=float(i)
            filtered_datas.append(element)
        filtered_datas=np.array(filtered_datas).reshape(1,-1)
        print(filtered_datas)
        import joblib
        from sklearn.preprocessing import MinMaxScaler
        norm=MinMaxScaler()
        model=joblib.load("restaurantprediction.pkl")
        prediction=model.predict(filtered_datas)
        return f"<body style='background-color:rgb(31,3,49);display:flex; justify-content:center; align-content:center;'><h1 style='color:white;'>Revenue : {prediction}</h1></body>"
    return render_template("index.html")
@app.route("/Home", methods=["GET","POST"])
def home():
    return render_template("index.html")
@app.route("/Service", methods=["GET","POST"])
def Service():
    return """
    <body style='background-color: rgb(218, 218, 236);
        margin-top:4%;
        margin-left:3%;'>
        <h2 style='color: black;
        background-color: rgb(218, 218, 236);
        margin-bottom:3%;
        '>This is for Restaurnt prediction<br>
         </h2>
         <div>
            <div>
                <p style='color:black;
                font-size:130%;'>View file</p>
                <p style='color:black;
                font-size:100%;'>Opens data in excel file</p>
            </div>
            <br>
            <div>
                <p style='color:black;
                font-size:130%;'>Know model</p>
                <p style='color:black;
                font-size:100%;'>Gives info about model used for prediction</p>
            </div>
            <br>
            <div>
                <p style='color:black;
                font-size:130%;'>Add</p>
                <p style='color:black;
                font-size:100%;'>Enter data for prediction </p>
            </div>
        </div>
    </body>"""
@app.route("/Contact", methods=["GET","POST"])
def Contact():
    return """
    <body style='background-color: rgb(218, 218, 236);
        margin-top:4%;
        margin-left:3%;'>
        <h2 style='color: black;
        background-color: rgb(218, 218, 236);
        margin-bottom:2.4%;
        '>Contact</h2>
        <div>
            <p style='color:black;
            font-size:110%;'>Mail : ytuseruser453@gmail.com<br></p>
        </div>
    </body>"""
@app.route("/About", methods=["GET","POST"])
def About():
    return """
    <body style='background-color: rgb(218, 218, 236);
        margin-top:4%;
        margin-left:3%;'>
        <h2 style='color: black;
        background-color: rgb(218, 218, 236);
        margin-bottom:2.4%;
        '>About</h2>
        <div style:'margin-top:5%;
        margin-left:5%;
        width:30%;
        heigth:30%;'>
            <p style='color:black;
            font-size:110%;'>restaurant predciton is for predicting the revenue: <br><br>
            By Useing RandomForestRegressor model<br><br>
            Its a Supervised Machine Learning Technique<br><br>
            </p>
            </div>
    </body>"""
 
if __name__=="__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)