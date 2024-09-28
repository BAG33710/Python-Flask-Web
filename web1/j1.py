from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/a')
def a():
    return render_template('a.html')

@app.route('/rus')
def rus():
    return render_template('rus.html')

@app.route('/eng')
def eng():
    return render_template('eng.html')

@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/image')
def image():
    return render_template('image.html')

if __name__ == '__main__':
    app.run()