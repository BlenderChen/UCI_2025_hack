from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def posts():
    return render_template('')
@app.route('/home/<string:name>')
def hello(name):
    return "Hello, " + name + "'s world."
@app.route('/onlyget', methods = ['POST'])
def get_req():
    return 'You can only get this webpage.'
if __name__ == '__main__':
    app.run(debug = True)