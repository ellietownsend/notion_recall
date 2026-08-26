from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', message="This data came from Python!")

@app.route("/upload_notes", methods=['GET', 'POST'])
def upload_notes():
    return "<p>Getting sent to python!</p>"

if __name__ == '__main__':
    app.run(debug=True)
