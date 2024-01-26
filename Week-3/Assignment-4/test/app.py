from flask import Flask, render_template, make_response, redirect, url_for, request

app = Flask(__name__)

@app.route('/myName', methods=['GET', 'POST'])
def my_name():
    user_name = request.cookies.get('user_name')

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            response = make_response(redirect(url_for('my_name')))
            response.set_cookie('user_name', user_input)
            return response

    if user_name:
        return render_template("my_name.html", user_name=user_name)
    
    return render_template("my_name.html", user_name=None)

@app.route('/trackName', methods=['GET'])
def track_name():
    user_input = request.args.get('name')

    if user_input:
        response = make_response(redirect(url_for('my_name')))
        response.set_cookie('user_name', user_input)
        return response

    return "Invalid request. Please provide a valid name."

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
