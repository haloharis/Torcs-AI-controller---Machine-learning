# Torcs

Here is a well-structured and visually appealing `README.md` for your GitHub repository:

---

# 🏎️ TORCS-AI-Racer

**Autonomous Racing Controller using Python & Machine Learning**

A data-driven AI controller built for [TORCS (The Open Racing Car Simulator)](http://torcs.sourceforge.net/), trained to predict throttle, brake, and steering commands using real-time sensor inputs.

---

## 📌 Objective

The goal of this project is to train a machine learning-based autonomous controller that can **drive a simulated car in TORCS**.
Using a neural network trained on **human driving data**, the model learns to map telemetry sensor inputs to control actions in real time.

---

## 📊 Data Collection Process

Manual driving sessions were performed in TORCS using `pyclient.py`, which logged telemetry and driver control data into `telemetry_log.csv`.

**Sensor Inputs Collected:**

* `speedX`, `speedY`, `speedZ` – Velocity in different axes
* `rpm` – Engine revolutions per minute
* `gear` – Current transmission gear
* `trackPos` – Lateral position on track
* `angle` – Angle between car’s heading and track axis

**Control Outputs Recorded:**

* `accelerate` – Throttle (0.0 to 1.0)
* `brake` – Braking force (0.0 to 1.0)
* `steer` – Steering angle (−1.0 to 1.0)

---

## 🧹 Data Preprocessing

Preprocessing steps handled in `train_model.py`:

1. **Cleaning**

   * Removed rows with missing values using `df.dropna()`

2. **Feature Selection**

   * Chosen features:
     `['speedX', 'speedY', 'speedZ', 'rpm', 'gear', 'trackPos', 'angle']`

3. **Normalization**

   * Applied `StandardScaler` to normalize input features

4. **Train-Test Split**

   * 90% training / 10% testing split using `train_test_split`

---

## 🧠 Model Architecture & Training

A feedforward neural network was implemented using Scikit-learn’s `MLPRegressor`.

| Component      | Configuration                   |
| -------------- | ------------------------------- |
| Hidden Layers  | 2 hidden layers (64 units each) |
| Activation     | ReLU                            |
| Optimizer      | Adam                            |
| Max Iterations | 300 epochs                      |
| Output Targets | `accelerate`, `brake`, `steer`  |

✅ Model and scaler are saved as:

* `torcs_mlp_model.pkl`
* `input_scaler.pkl`

---

## 🤖 Autonomous Controller Integration

The controller logic is implemented in `autoDrive.py`, within the `AutonomousDriver` class.

### 🔁 Runtime Workflow:

1. **Sensor Parsing** – Convert TORCS string input to key-value dictionary
2. **Input Preparation** – Extract features and reshape to model format
3. **Scaling** – Normalize inputs using the saved `StandardScaler`
4. **Prediction** – MLP model outputs control signals
5. **Gear Logic** – A rule-based system selects the appropriate gear
6. **Command Output** – Formatted as:

```bash
(accel X) (brake Y) (steer Z) (gear N)
```

... and sent back to the simulator.

---

## 🚀 Results & Summary

This project demonstrates a successful integration of supervised learning and real-time control in a racing simulator.
The MLP controller effectively replicates human-like driving behavior.

### 🔧 Future Enhancements

* Collect diverse driving data (varied tracks, conditions)
* Replace rule-based gear logic with a learned model
* Explore **deep reinforcement learning** for adaptive behavior

---

## 📁 Repository Structure

```
.
├── pyclient.py           # Connects to TORCS and collects telemetry
├── telemetry_log.csv     # Recorded driving data
├── train_model.py        # Data preprocessing and MLP training
├── autoDrive.py          # Autonomous controller logic
├── torcs_mlp_model.pkl   # Trained model
├── input_scaler.pkl      # Scaler for input normalization
└── README.md             # Project overview
```

---

## 🧠 Tools & Libraries Used

* Python 3.x
* [TORCS Simulator](http://torcs.sourceforge.net/)
* Scikit-learn (MLPRegressor, StandardScaler)
* NumPy, Pandas

---

## 💡 Author

**\[Your Name]** – *AI/ML Enthusiast | Autonomous Systems Developer*

---

## 📜 License

This project is licensed under the MIT License.
See [`LICENSE`](LICENSE) for more information.

---

Let me know if you'd like badges, a demo video/GIF section, or project logo added!
