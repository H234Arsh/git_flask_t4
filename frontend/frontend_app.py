from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
