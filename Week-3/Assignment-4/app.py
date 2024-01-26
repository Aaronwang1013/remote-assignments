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


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)