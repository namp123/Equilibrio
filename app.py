from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump,load
app = Flask(__name__)

@app.route('/',methods=['GET','POST']) #renders onto 127.0.0.1:5000
def view1():#view function 1
    return render_template("app.html")

@app.route('/questionnaire')
def view2():
    return render_template("questionnaire.html")

@app.route('/appsubmission',methods=['GET','POST'])
def view3():
    if request.method=="POST":
        Fname=str(request.form.get('name1'))
        Lname=str(request.form.get('name2'))
        Age=request.form.get('age')
        if request.form.get('choice')=='Male':
            Gender=1
        else:
            Gender=0
        if request.form.get('op1')=='Yes':
            Q1=1
        else:
            Q1=0
        if request.form.get('op2')=='Yes':
            Q2=1
        else:
            Q2=0
        if request.form.get('op3')=='Yes':
            Q3=1
        else:
            Q3=0
        if request.form.get('op4')=='Yes':
            Q4=1
        else:
            Q4=0
        if request.form.get('op5')=='Yes':
            Q5=1
        else:
            Q5=0
        if request.form.get('op6')=='Yes':
            Q6=1
        else:
            Q6=0
        if request.form.get('op7')=='Yes':
            Q7=1
        else:
            Q7=0
        if request.form.get('op8')=='Yes':
            Q8=1
        else:
            Q8=0
        if request.form.get('op9')=='Yes':
            Q9=1
        else:
            Q9=0
        if request.form.get('op10')=='Yes':
            Q10=1
        else:
            Q10=0
        if request.form.get('op11')=='Yes':
            Q11=1
        else:
            Q11=0
        if request.form.get('op12')=='Yes':
            Q12=1
        else:
            Q12=0
        if request.form.get('op13')=='Yes':
            Q13=1
        else:
            Q13=0
        if request.form.get('op14')=='Yes':
            Q14=1
        else:
            Q14=0
        if request.form.get('op15')=='Yes':
            Q15=1
        else:
            Q15=0
        user_input=np.array([[Age,Gender,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15]])
        model=load("rfc.joblib")
        prediction_rfc=model.predict(user_input)
        if prediction_rfc==1:
            result="You are experiencing higher levels of Anxiety, please consult a proffesional for further help."
        else:
            result="Your anxiety is at a subsidised level."
        if Gender==1:
            Gender="Male"
        else:
            Gender="Female"
        return render_template("appsubmission.html",Fname=Fname,Lname=Lname,Age=Age,Gender=Gender,Result=result)
    else:
        return render_template("appsubmission.html")



if __name__=="__main__":
    app.run(debug=True)
