from flask import Flask, render_template, request
from model import analyze_personality

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    result = analyze_personality(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)