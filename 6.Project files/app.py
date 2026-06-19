from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import numpy as np
import pickle
import os
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "ids_secret_key_2024"
app.permanent_session_lifetime = timedelta(minutes=30)

# -------------------------------------------------------
# Load pre-trained ML model (if available)
# -------------------------------------------------------
MODEL_PATH = os.path.join("models", "ids_model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")

model = None
scaler = None

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
if os.path.exists(SCALER_PATH):
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

# -------------------------------------------------------
# Attack label mapping
# -------------------------------------------------------
ATTACK_LABELS = {
    0: "Normal",
    1: "DoS Attack",
    2: "Probe / Scan",
    3: "R2L Attack",
    4: "U2R Attack"
}

# -------------------------------------------------------
# In-memory alert log (replace with DB in production)
# -------------------------------------------------------
alert_log = []

# -------------------------------------------------------
# Routes
# -------------------------------------------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    stats = {
        "total_alerts": len(alert_log),
        "attack_count": sum(1 for a in alert_log if a["label"] != "Normal"),
        "normal_count": sum(1 for a in alert_log if a["label"] == "Normal"),
        "recent_alerts": alert_log[-10:][::-1]
    }
    return render_template("dashboard.html", stats=stats)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None
    if request.method == "POST":
        try:
            # Collect network traffic features from form
            features = [
                float(request.form.get("duration", 0)),
                float(request.form.get("src_bytes", 0)),
                float(request.form.get("dst_bytes", 0)),
                float(request.form.get("land", 0)),
                float(request.form.get("wrong_fragment", 0)),
                float(request.form.get("urgent", 0)),
                float(request.form.get("hot", 0)),
                float(request.form.get("num_failed_logins", 0)),
                float(request.form.get("logged_in", 0)),
                float(request.form.get("num_compromised", 0)),
            ]

            if model is not None and scaler is not None:
                features_scaled = scaler.transform([features])
                prediction = model.predict(features_scaled)[0]
                confidence = max(model.predict_proba(features_scaled)[0]) * 100
                label = ATTACK_LABELS.get(int(prediction), "Unknown")
            else:
                # Demo mode: rule-based simple detection
                src_bytes = features[1]
                dst_bytes = features[2]
                failed_logins = features[7]

                if failed_logins > 3:
                    label = "R2L Attack"
                    confidence = 87.5
                elif src_bytes > 100000:
                    label = "DoS Attack"
                    confidence = 92.3
                elif src_bytes == 0 and dst_bytes == 0:
                    label = "Probe / Scan"
                    confidence = 78.0
                else:
                    label = "Normal"
                    confidence = 95.6

            # Log the alert
            alert_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "label": label,
                "confidence": round(confidence, 2),
                "features": features
            }
            alert_log.append(alert_entry)

            result = {
                "label": label,
                "confidence": round(confidence, 2),
                "is_attack": label != "Normal",
                "timestamp": alert_entry["timestamp"]
            }
            flash(f"Prediction: {label} ({confidence:.1f}% confidence)", "success" if label == "Normal" else "danger")

        except Exception as e:
            flash(f"Error during prediction: {str(e)}", "danger")

    return render_template("predict.html", result=result)


@app.route("/alerts")
def alerts():
    return render_template("alerts.html", alerts=alert_log[::-1])


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """REST API endpoint for real-time prediction"""
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Missing features"}), 400

    features = data["features"]
    # Demo rule-based detection
    src_bytes = features[1] if len(features) > 1 else 0
    failed_logins = features[7] if len(features) > 7 else 0

    if failed_logins > 3:
        label, confidence = "R2L Attack", 87.5
    elif src_bytes > 100000:
        label, confidence = "DoS Attack", 92.3
    else:
        label, confidence = "Normal", 95.6

    return jsonify({
        "label": label,
        "confidence": confidence,
        "is_attack": label != "Normal",
        "timestamp": datetime.now().isoformat()
    })


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
