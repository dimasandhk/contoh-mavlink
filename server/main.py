from flask import Flask, request, jsonify
from dronekit import connect

app = Flask(__name__)

vehicle = connect("tcp:127.0.0.1:14550", wait_ready=True)
vehicle.wait_ready("autopilot_version")

@app.route("/get_all_params", methods=['GET'])
def get_all_params():
    try:
        params = {param: value for param, value in vehicle.parameters.items()}        
        return jsonify(params), 402
    except Exception as e:
        return jsonify(ok=False)
    
app.run(debug=True)