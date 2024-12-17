from flask import Flask, jsonify
from datetime import datetime, timedelta  
import time

app = Flask(__name__)

# Human-readable simulation start time
simulation_start_str = "2024-01-01 00:00:00"  # Set your simulation start time here
simulation_start_dt = datetime.strptime(simulation_start_str, "%Y-%m-%d %H:%M:%S")  # Convert to datetime
simulation_start = simulation_start_dt.timestamp()  # Convert to system timestamp

# Time scaling factor
time_scale = 10  # Simulated time moves 10x faster

@app.route('/time', methods=['GET'])
def get_simulated_time():
    """Calculate and return the simulated time."""
    current_real_time = time.time()
    time_elapsed = current_real_time - simulation_start  # Real elapsed time
    simulated_time_seconds = time_elapsed * time_scale  # Scale time
    
    # Add simulated time to the human-readable simulation start
    simulated_dt = simulation_start_dt + timedelta(seconds=simulated_time_seconds)
    formatted_simulated_time = simulated_dt.strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({"simulated_time": formatted_simulated_time})

if __name__ == '__main__':
    print("Web service running on http://localhost:5000/time")
    app.run(debug=True)
