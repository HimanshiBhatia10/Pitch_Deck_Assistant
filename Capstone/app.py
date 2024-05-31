from flask import Flask, render_template, request, jsonify
import numpy as np
from werkzeug.utils import secure_filename
import os


def fetch_summary(name):
    path = "/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/summary"
    summ = None  # Initialize summ to None
    for summary in os.listdir(path):
        if name[:-4] == summary[:-4]:
            with open(os.path.join(path, summary), 'r') as file:  # Use 'with' to ensure file is properly closed
                summ = file.read()
            break  # Exit the loop once a match is found
    if summ is None:  # Handle case where no match is found
        return "Summary not found"
    return summ


app = Flask(__name__)
# Creates instance of Flask class.
# '__name__' is a variable that holds the name of the current python module/ script.
# script: Where the current python code of Flask is written.

app.config['UPLOAD_FOLDER'] = r'/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/Capstone/uploads'


@app.route('/')  # Route: Binds to a URL and runs the function below.
def index():
    return render_template('Pitch_deck.html')


# render_template: Helps to render the html file.
# rendering: refers to generating a final output by replacing a template with actual code.

@app.route('/upload', methods=['POST'])
def home():
    if 'pdfFile' not in request.files:
        return jsonify({"error": "No file part"}), 400

    files = request.files.getlist('pdfFile')
    results = []
    # request: handles incoming form data.
    for file in files:
        if file.filename == '':
            return jsonify({"error": "No file part"}), 400
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            summary = fetch_summary(filename)
            results.append({"filename": filename, "summary": summary})
    return jsonify(results)


if __name__ == "__main__":  # '__name__' is set to '__main__' if the current python file is run directly.
    app.run(debug=True)