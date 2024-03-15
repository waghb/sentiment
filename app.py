from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@api_key = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_api_key', methods=['POST'])
def store_api_key():
    global api_key
    api_key = request.json.get('apiKey')
    print(f"Received API key: {api_key}")  # Debug statement
    return jsonify({'message': 'API key stored successfully!'})

@app.route('/analyze')
def analyze():
    global api_key
    print(f"Current API key: {api_key}")  # Debug statement
    if api_key:
        # Call api.py with the stored API key
        print("Calling api.py")  # Debug statement
        subprocess.run(["python3", "api.py", api_key])
        return 'Analysis completed!'
    else:
        return 'API key not provided. Please submit the API key first.'

if __name__ == '__main__':
    app.run(debug=True)
