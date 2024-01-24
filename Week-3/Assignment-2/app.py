from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, My Server!"


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