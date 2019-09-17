# /index.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# run Flask app
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
