from flask import Flask, request, jsonify
import requests
import sqlite3

app = Flask(__name__)

SIMULATED_API_URL = "http://127.0.0.1:5000/energy-data"  # Replace with actual URL if different

def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS energy (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        device_id TEXT,
                        timestamp TEXT,
                        energy REAL,
                        UNIQUE(device_id, timestamp)  -- Prevent duplicate entries
                    )''')
    conn.commit()
    conn.close()

@app.route("/api/energy", methods=["POST"])
def fetch_simulated_energy_data():
    try:
        print("Fetching simulated energy data...", flush=True)
        response = requests.get(SIMULATED_API_URL)
        print(f"API Response Status Code: {response.status_code}", flush=True)

        if response.status_code == 200:
            energy_data = response.json()
            print("Fetched Energy Data:", energy_data, flush=True)

            conn = sqlite3.connect("energy_data.db")
            cursor = conn.cursor()

            for data in energy_data:
                sql_query = f"INSERT INTO energy (device_id, timestamp, energy) VALUES ('{data['device_id']}', '{data['timestamp']}', {data['energy_kwh']})"
                print("Executing SQL:", sql_query, flush=True)  # Debugging
                try:
                    cursor.execute(sql_query)
                except sqlite3.IntegrityError as e:
                    print(f"Duplicate entry error: {e}", flush=True)

            conn.commit()
            conn.close()
            print("Data successfully stored in database", flush=True)
            return jsonify({"message": "Simulated energy data stored"}), 201
        else:
            print("Failed to fetch data from API", flush=True)
            return jsonify({"error": "Failed to fetch data"}), 500

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", flush=True)
        return jsonify({"error": str(e)}), 500




@app.route("/api/energy/<device_id>", methods=["GET"])
def get_energy_data(device_id):
    """Retrieve energy data for a specific device"""
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, energy FROM energy WHERE device_id = ? ORDER BY timestamp DESC LIMIT 10", (device_id,))
    data = [{"timestamp": row[0], "energy": row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    init_db()  # Ensure the database is initialized
    with app.app_context():  # Set up the application context
        fetch_simulated_energy_data()
    app.run(debug=True)