from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', message="Welcome to notion recall!")

@app.route("/upload_notes", methods=['GET', 'POST'])
def upload_notes():
    if request.method == "POST":
        notes = request.form.get("notes")
        return f"""
            <h1>Notes recieved: {notes} </h1>
        """

    return """
    <form method = "POST" action = "">
        <label>Upload a file of your notes:</label>
            <input type = "file" 
                    id = "notes" 
                    name = "notes" 
                    accept = "text/html, .html, .htm" />
                <button type = "submit">Send notes off!</button>
        </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
