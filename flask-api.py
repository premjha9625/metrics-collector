import csv
from flask import Flask, render_template, request, jsonify
from subprocess import Popen, PIPE
from subprocess import check_output
from flask_cors import CORS
import tablib
import os

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
        if (password == ''):
            stdout = check_output(['/home/PremJha/Desktop/python-script/shellwopass.sh',ip_address, user]).decode('utf-8')

            # Return output of the shell script as the API response
            return stdout
        else:
            stdout = check_output(['/home/PremJha/Desktop/python-script/shell.sh',ip_address, user, password ]).decode('utf-8')

            # Return output of the shell script as the API response
            return stdout
            

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#api for csv reading

dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'/home/prem/Desktop/metrics/dev/disk_usage.csv')) as f:
    dataset.csv = f.read()
@app.route('/csv', methods=['GET'])
def display_csv():
    # csv_data = []

    # # Read the CSV file and store its content in csv_data list
    # with open('/home/prem/Desktop/metrics/dev/disk_usage.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         csv_data.append(row)

    # # Render the template and pass the CSV data to it
    # return render_template('/home/prem/Desktop/metrics/dev/csv_template.html', csv_data=csv_data)
 
    return dataset.html  


if __name__ == '__main__':
    app.run(debug=True, port=5000)
