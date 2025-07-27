# Federated Learning with Differential Privacy for Secure Data Collaboration

This project implements a secure and privacy-preserving Federated Learning (FL) system enhanced with Differential Privacy (DP). The goal is to enable multiple clients (e.g., hospitals, banks, mobile devices) to collaboratively train a machine learning model without sharing raw data. The central server coordinates training by aggregating encrypted or noise-added model updates from clients. This ensures data confidentiality while still allowing useful, high-accuracy model training. A Flask-based web interface allows users to initiate training, view model progress, and visualize accuracy metrics over multiple federated rounds.

---

## 🌟 Key Features

- ✅ **Federated Learning (FL):** Decentralized model training across multiple clients with local data.
- 🔐 **Differential Privacy (DP):** Adds noise to protect individual data points from being inferred.
- 📶 **Secure Aggregation:** Clients send only privatized model weights to the central server.
- 📊 **Visualization:** Real-time training curves and accuracy logs shown via a web interface.
- 💻 **Multi-Client Simulation:** Includes multiple simulated clients (e.g., `client1.py`, `client2.py`).
- 🔁 **Global Model Updates:** Central server performs Federated Averaging after each round.
- ⚙️ **Lightweight & Fast:** TinyCNN ensures fast training even in constrained environments.
- 📁 **Modular Design:** Easily extendable to add more clients or support other models/datasets.

---

## 💻 Technologies Used

- **Python 3.8+** – Core programming language.
- **PyTorch** – For building and training the deep learning model.
- **Opacus** – For implementing Differential Privacy with PyTorch.
- **Flask** – Lightweight Python web framework for the user interface.
- **Chart.js** – JavaScript library for training visualization on the web.
- **NumPy & Pandas** – Data manipulation and analysis.
- **Matplotlib / Seaborn** – Optional for offline graph generation.
- **HTML, CSS, JavaScript** – Frontend interface for displaying training logs.

---

## ⚙️ How It Works

1. **Client Initialization:** Each client loads its local dataset (e.g., MNIST), initializes the model, and starts local training.
2. **Local Training:** Clients train the model locally for a few epochs using their private data.
3. **Differential Privacy:** Noise is added to model weights or gradients using Opacus to ensure privacy.
4. **Model Communication:** Clients serialize and send the privatized model updates to the central server.
5. **Aggregation:** The server performs Federated Averaging to combine updates and build a new global model.
6. **Model Distribution:** The updated global model is redistributed to clients for the next round.
7. **Visualization:** Training rounds and accuracy progress are shown live on the Flask-based dashboard.
8. **Repeat:** Steps 2–7 are repeated over multiple communication rounds until convergence.


