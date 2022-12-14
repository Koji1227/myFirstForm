from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/procForm', methods = ['POST'])
def processPost():
    x = int(request.form['x'])
    y = int(request.form['y'])
    sum = x + y
    return render_template('result.html', result = f"答えは{sum}です。")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)