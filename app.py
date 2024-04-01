from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@api_key = None

@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

api_key = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    global api_key
    try:
        # Store the API key from the request
        api_key = request.json.get('apiKey')
        print(f"Received API key: {api_key}")  # Debug statement
        
        if api_key:
            # Call api.py with the stored API key
            print("Calling api.py")  # Debug statement
            subprocess.run(["python3", "api.py", api_key])
            return 'Analysis completed!'
        else:
            return 'API key not provided. Please submit the API key first.', 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
