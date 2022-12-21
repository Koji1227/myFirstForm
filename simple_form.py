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
    dif = x - y
    pro = x * y
    quo = x / y
    return render_template('result.html', result = f"{x}足す{y}の答えは{sum}です。{x}引く{y}の答えは{dif}です。{x}掛ける{y}の答えは{pro}です。{x}割る{y}の答えは{quo}です。")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)