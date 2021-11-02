from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
#import csv
import pandas as pd

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/data',methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        df = pd.read_csv(f,index_col=[0])
        filename = 'random_forest.pkl'
        #data =[]
        #with open(f) as file:
        #    csvfile = csv.reader(file)
        #    for rows in csvfile:
        #        data.append(rows)

        loaded_model = pickle.load(open(filename,'rb'))
        data = loaded_model.predict(df)
        return render_template("data.html",data=data)





if __name__ =='__main__':
    app.run(debug=True)