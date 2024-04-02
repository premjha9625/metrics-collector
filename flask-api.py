from ast import Index
import csv
from flask import Flask, render_template, request, jsonify
from subprocess import Popen, PIPE
from subprocess import check_output
from flask_cors import CORS
# import tablib
# import os
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# CORS(app, resources={r"/run_script": {"origins": "*"}})
# CORS(app, resources={r"csv": {"origins": "*"}})

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

#1st method to read

# dataset = tablib.Dataset()
# with open(os.path.join(os.path.dirname(__file__),'/home/prem/Desktop/metrics/dev/disk_usage.csv')) as f:
#     dataset.csv = f.read()
@app.route('/getDisk', methods=['GET'])
def display_csv():
    
    #2nd method to read and return as html template
    
    # csv_data = []
    # # Read the CSV file and store its content in csv_data list
    # with open('/home/prem/Desktop/metrics/dev/disk_usage.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         csv_data.append(row)

    # # Render the template and pass the CSV data to it
    # return render_template('/home/prem/Desktop/metrics/dev/csv_template.html', csv_data=csv_data)
    
    #3rd method to read and return as json
    # read_csv = pd.read_csv('/home/prem/Desktop/metrics/dev/disk_usage.csv',delimiter= ',') # or delimiter = ';'
    # read_csv.head() # display your data and check it
    # csv_to_json = read_csv.to_json(orient = 'columns')
    # return jsonify(csv_to_json) 

    #4th method to read and return as json
    cols = ['Filesystem','Type','Size','Used','Available','Use%','Mounted on']
    read_csv = pd.read_csv('/home/PremJha/Desktop/python-script/disk_usage.csv', delimiter=',')
    csv_dict = read_csv.to_dict(orient='records')
    return jsonify(csv_dict)


@app.route('/getMemory', methods=['GET'])
def display_memory():
    cols = ["total","used","free","available","used%"]
    read_csv = pd.read_csv('/home/PremJha/Desktop/python-script/ram_usage.csv', delimiter=',')
    csv_dict = read_csv.to_dict(orient='records')
    return jsonify(csv_dict)

@app.route('/getCPU', methods=['GET'])
def display_cpu():
    cols = ["total","used","free","available","used%"]
    read_csv = pd.read_csv('/home/PremJha/Desktop/python-script/ram_usage.csv', delimiter=',')
    csv_dict = read_csv.to_dict(orient='records')
    return jsonify(csv_dict)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
