from flask import Flask, request, jsonify
from subprocess import Popen, PIPE
from subprocess import check_output
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/run_script": {"origins": "*"}})

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Extract IP address and user from the request
        ip_address = request.json.get('ip_address')
        user = request.json.get('user')
        password = request.json.get('password')

        # Validate parameters
        if not ip_address or not user:
            return jsonify({'error': 'IP address and user are required parameters.'}), 400

        # Execute shell script with parameters
        #result = subprocess.run(['/home/PremJha/Desktop/python-script/shell.sh', ip_address, user])
        stdout = check_output(['/home/PremJha/Desktop/python-script/shell.sh',ip_address, user, password ]).decode('utf-8')

        # Return output of the shell script as the API response
        return stdout
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
