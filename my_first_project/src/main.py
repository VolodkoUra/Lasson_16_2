from flask import Flask, session, render_template, request
app = Flask(__name__, template_folder='tempates')

@app.route('/')   # создаём енд поинт
def hello_world():
    return 'Hello World'


@app.route('/first_template',methods=['GET', 'POST'])
def first_temolate():
    if request.method == 'GET':
        return render_template('ft.html')
    elif request.method == 'POST':
        print(request)
        return 'Good'

@app.route('/new_data')
def new_data():
    return ''


if __name__ == '__main__':
    app.run('127.0.0.1', 5050)