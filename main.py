# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib 

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

regression_model = joblib.load('linear_regression.pickle')

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        distance = request.form['distance']
        quantity = request.form['quantity']
        shipping = request.form['shipping']

        if shipping == 'Free':
            ship = 2
        else:
            ship = 1

        print(distance, quantity, shipping, ship)

        input = np.array([[distance,quantity, ship]],dtype='float')
        time = np.ceil(float(regression_model.predict(input)))
        
    return render_template("result.html",time = time)

if __name__ == '__main__':
    app.run(debug=True)
