from flask import Flask, render_template, request, url_for
import parser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', message="Welcome to notion recall!")

@app.route("/upload_notes", methods=['GET', 'POST'])
def upload_notes():

    if request.method == "POST":
        uploaded_notes = request.files.get('notes')
        assert uploaded_notes is not None
        if upload_notes and uploaded_notes.filename != '':
            file_content = uploaded_notes.read().decode('utf-8')
            return f"File contents loaded successfully:\n\n{file_content}"

    return """
    <form method = "POST" action = "" enctype="multipart/form-data">
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
