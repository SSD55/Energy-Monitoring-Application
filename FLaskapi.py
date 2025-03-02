from flask import Flask, jsonify
from flask_cors import CORS  
import random
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Sample appliances with device IDs
appliances = [
    {"device_id": "A001", "name": "Refrigerator", "min_power": 50, "max_power": 150},
    {"device_id": "A002", "name": "Washing Machine", "min_power": 500, "max_power": 1200},
    {"device_id": "A003", "name": "Air Conditioner", "min_power": 800, "max_power": 2000},
    {"device_id": "A004", "name": "TV", "min_power": 50, "max_power": 200},
    {"device_id": "A005", "name": "Heater", "min_power": 1000, "max_power": 2500},
    {"device_id": "A006", "name": "Microwave", "min_power": 600, "max_power": 1200}
]

def generate_energy_data():
    """Generate simulated energy consumption data with multiple timestamps per device"""
    data = []
    
    for appliance in appliances:
        for i in range(5):  # Generate 5 timestamps per device
            power_usage = random.randint(appliance["min_power"], appliance["max_power"])  # Watts
            energy_kwh = round((power_usage / 1000) * 1, 4)  # ⚡ Energy for 1 hour
            
            timestamp = (datetime.datetime.now() - datetime.timedelta(minutes=i * 10)).isoformat()

            data.append({
                "device_id": appliance["device_id"],
                "energy_kwh": energy_kwh,  # 🚀 Higher energy values
                "timestamp": timestamp
            })
    
    return data

@app.route('/energy-data', methods=['GET'])
def get_energy_data():
    """API endpoint to get simulated appliance energy data"""
    return jsonify(generate_energy_data())

if __name__ == '__main__':
    app.run(debug=True)
