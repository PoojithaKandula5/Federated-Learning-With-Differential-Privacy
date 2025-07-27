# app.py
from flask import Flask, render_template, jsonify
import subprocess
import threading
import time

app = Flask(__name__)
training_logs = []
accuracy_log = []

def run_training():
    global training_logs, accuracy_log
    training_logs.clear()
    accuracy_log.clear()

    rounds = 5
    for rnd in range(1, rounds + 1):
        log_entry = f"--- Round {rnd} ---"
        training_logs.append(log_entry)

        for cid in range(1, 5):  # Clients 1–4
            script = f"client{cid}.py"
            training_logs.append(f"[Client {cid}] Training started...")
            result = subprocess.run(["python", script], capture_output=True, text=True)
            training_logs.extend(result.stdout.strip().split('\n'))
            training_logs.append(f"[Client {cid}] Update sent to server.")

        training_logs.append(f"[Server] Aggregated updates for Round {rnd}")
        accuracy = 85 + rnd  # Simulated for now
        accuracy_log.append({"round": rnd, "accuracy": accuracy})
        training_logs.append(f"[Server] Accuracy after Round {rnd}: {accuracy}%")
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-training', methods=['POST'])
def start_training():
    thread = threading.Thread(target=run_training)
    thread.start()
    return jsonify({"status": "Training started"})

@app.route('/logs')
def get_logs():
    return jsonify(training_logs)

@app.route('/accuracy')
def get_accuracy():
    return jsonify(accuracy_log)

if __name__ == '__main__':
    app.run(debug=True)
