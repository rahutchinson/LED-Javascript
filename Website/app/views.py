from app import app
from flask import render_template, request

command_history = []

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    if request.form:
        input_string = request.form['input']
        try:
            result = str(eval(input_string))
        except:
            result = "Error in input syntax"

        command_history.insert(0,(input_string, result))

        return render_template('index.html',
                               title='Home',
                               result=result,
                               history=command_history)
    else:
        return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return 'This page might exist in the future'