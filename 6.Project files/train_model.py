"""
train_model.py
--------------
Train a Random Forest classifier on a synthetic NSL-KDD-like dataset
and save the model + scaler to the 'models/' directory.

Run this ONCE before starting the Flask app:
    python train_model.py
"""

import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# -------------------------------------------------------
# Generate synthetic training data (NSL-KDD feature subset)
# -------------------------------------------------------
np.random.seed(42)
N = 5000

# Features: duration, src_bytes, dst_bytes, land, wrong_fragment,
#           urgent, hot, num_failed_logins, logged_in, num_compromised

def generate_samples(n, label):
    if label == 0:  # Normal
        return np.column_stack([
            np.random.randint(0, 100, n),
            np.random.randint(0, 10000, n),
            np.random.randint(0, 10000, n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.random.randint(0, 5, n),
            np.zeros(n),
            np.ones(n),
            np.zeros(n)
        ])
    elif label == 1:  # DoS
        return np.column_stack([
            np.zeros(n),
            np.random.randint(100000, 600000, n),
            np.zeros(n),
            np.zeros(n),
            np.random.randint(0, 4, n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n)
        ])
    elif label == 2:  # Probe
        return np.column_stack([
            np.random.randint(0, 5, n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n)
        ])
    elif label == 3:  # R2L
        return np.column_stack([
            np.random.randint(1, 30, n),
            np.random.randint(100, 500, n),
            np.random.randint(100, 500, n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.random.randint(0, 3, n),
            np.random.randint(4, 10, n),
            np.zeros(n),
            np.zeros(n)
        ])
    else:  # U2R (label=4)
        return np.column_stack([
            np.random.randint(0, 10, n),
            np.random.randint(200, 1000, n),
            np.random.randint(200, 1000, n),
            np.zeros(n),
            np.zeros(n),
            np.zeros(n),
            np.random.randint(5, 20, n),
            np.random.randint(0, 2, n),
            np.ones(n),
            np.random.randint(1, 10, n)
        ])

X_list, y_list = [], []
counts = {0: 2000, 1: 1000, 2: 800, 3: 700, 4: 500}
for label, count in counts.items():
    X_list.append(generate_samples(count, label))
    y_list.extend([label] * count)

X = np.vstack(X_list)
y = np.array(y_list)

# -------------------------------------------------------
# Train/test split & scaling
# -------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# -------------------------------------------------------
# Train model
# -------------------------------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {acc * 100:.2f}%\n")
print(classification_report(y_test, y_pred,
      target_names=["Normal", "DoS", "Probe", "R2L", "U2R"]))

# -------------------------------------------------------
# Save model and scaler
# -------------------------------------------------------
os.makedirs("models", exist_ok=True)
with open("models/ids_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model saved to models/ids_model.pkl")
print("✅ Scaler saved to models/scaler.pkl")
