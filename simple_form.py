from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/procForm', methods = ['POST'])
def processPost():
    msg = request.form['msg']
    return render_template('result.html', message = msg)

if __name__ == 'main':
    app.run(host = '0.0.0.0', port = 8000, debug = True)