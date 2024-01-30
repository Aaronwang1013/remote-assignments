from flask import Flask
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from flask import request
import json

app = Flask(__name__)


def get_save_data():
    try:
        data = json.loads(request.cookies.get('name'))
    except TypeError:
        data = {}
    return data

@app.route('/')
def index():
    return render_template("index.html")


#GET for the sum.html page, POST for submit the number
@app.route('/sum.html', methods=['GET','POST'])
def sum():
    return render_template("sum.html")

@app.route('/data')
def data():
    number = request.args.get('number')
    if number is None:
        return "Lack of Parameter"
    try:
        number = int(number)
        Sum = 0
        for i in range(1, number+1):
            Sum += i
        return "{}".format(Sum)
    except:
        return "Wrong Parameter"
    
@app.route('/myName')
def myName():
    data = get_save_data()
    return render_template("myName.html", saves=data)


@app.route('/trackName' , methods=['POST'])
def trackName():
    response = make_response(redirect(url_for('myName')))
    data = get_save_data()
    data.update(dict(request.form.items()))
    # print(data)
    response.set_cookie('name', json.dumps(data))
    return response



app.run(debug=True, port=3000, host='127.0.0.1')
