from flask import Flask
from flask import request, render_template

app = Flask(__name__)


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
    



app.run(debug=True, port=3000, host='127.0.0.1')
