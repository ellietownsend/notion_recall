from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', message="This data came from Python!")

if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route('/', methods=['GET', 'POST'])
def home():
    user_message = ""
    
    # Check if the user submitted the form
    if request.method == 'POST':
        # Grab data from the HTML input field using its 'name' attribute
        username = request.form.get('username')
        user_message = f"Hello, {username}! Your frontend is officially connected to Flask."
    
    # Send the HTML template back, along with an optional message variable
    return render_template('index.html', message=user_message)

if __name__ == '__main__':
    app.run(debug=True)
"""