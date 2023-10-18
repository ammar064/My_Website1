from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

import matplotlib

app = Flask(__name__)
model = pickle.load(open('insurance.pk1', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('insurance.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        BMI = float(request.form['BMI'])
        Age = int(request.form['Age'])
        Children = int(request.form['Children'])
        
        Smoker = int(request.form['Smoker'])
    
        Geography_Germany = request.form['Geography_Germany']
        if(Geography_Germany == 'Southwest'):
            Geography_Germany = 1
            
                
        elif(Geography_Germany == 'Southeast'):
            Geography_Germany = 2
            
        elif(Geography_Germany == 'Northwest'):
            Geography_Germany = 3   
        
        else:
            Geography_Germany = 4
            
        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        prediction = model.predict([[BMI,Age,Geography_Germany,Children,Smoker,Gender_Male]])
        
        return render_template('insurance.html',format(round(prediction[0],2)))
         
          
                
if __name__=="__main__":
    app.run(debug=True)
