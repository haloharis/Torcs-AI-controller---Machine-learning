# Torcs

1. Objective
The goal of this project is to train a machine learning-based controller that can drive a simulated
vehicle in TORCS (The Open Racing Car Simulator) by predicting throttle, brake, and steering
commands based on real-time sensor data. We use a data-driven approach where a neural
network model is trained on human-driven telemetry data to learn control mappings.
2. Data Collection Process
Telemetry data was collected during manual driving sessions in TORCS using the pyclient.py
script. This script listens to real-time sensor data such as:
 speedX, speedY, speedZ: representing the car's velocity in different directions.
 rpm: engine revolutions per minute.
 gear: current transmission gear.
 trackPos: lateral position of the car on the track.
 angle: angle between the car's heading and the track axis.
At the same time, driver inputs were recorded, including:
 accelerate: throttle (0.0 to 1.0)
 brake: braking force (0.0 to 1.0)
 steer: steering angle (−1.0 to 1.0)
The collected data was stored in a CSV file telemetry_log.csv, with each row representing a
timestamped instance of sensor readings and corresponding control inputs.
