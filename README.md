# 🛡️ AI-Enhanced Intrusion Detection System (IDS)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-purple?style=for-the-badge&logo=bootstrap)
![Status](https://img.shields.io/badge/Project-Production%20Ready-success?style=for-the-badge)

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=spsourabh17.AI-Enhanced-Intrusion-Detection-System)
---

## 📌 Project Overview

The **AI-Enhanced Intrusion Detection System (IDS)** is a machine learning-powered cybersecurity web application designed to inspect, log, and classify network anomalies in real time. 

Leveraging an optimized **Random Forest Classifier** trained on refined features from the industry-standard **NSL-KDD dataset**, the platform actively categorizes incoming network packets into safe or hostile traffic signatures. Built as a full-stack application using **Flask**, it features an interactive live analytics dashboard, real-time manual prediction entry, and detailed threat alerts logging.

---

## 🚀 Key Features & Capabilities

* **🔮 High-Accuracy ML Engine:** Uses an ensemble Random Forest model achieving **~96% accuracy** on network feature classifications.
* **📊 Analytics Dashboard:** Interactive data visualizations powered by **Chart.js** displaying total connection counts, security logs, and a dynamic threat-distribution doughnut chart.
* **🚨 Granular Attack Logging:** Tracks every threat event with categorical label mappings, precision confidence scores, and atomic execution timestamps.
* **⚡ On-Demand Traffic Simulator:** Features built-in macro buttons to inject instant simulation payloads (Normal, DoS, or R2L) for easy evaluation.

---

## 📊 Threat Matrix

The classification engine maps incoming traffic to five specific operational profiles:

| Profile Type | Vector Category | Target Threat Profile & Description |
| :--- | :--- | :--- |
| **DoS** | Denial of Service | Overwhelms computing resources to force system downtime or degradation. |
| **Probe** | Surveillance Scan | Mapping network topologies to discover vulnerable, open operational ports. |
| **R2L** | Remote to Local | Exploits structural loopholes to gain local machine privileges from an external node. |
| **U2R** | User to Root | Base privilege escalation targeting unauthorized superuser or root access rights. |
| **Normal** | Legitimate Traffic | Regular, compliant data packets behaving within standard network rules. |

---

## ⚙️ Technology Stack

* **Backend Framework:** Python, Flask, Werkzeug
* **Machine Learning & Analytics:** Scikit-Learn (Random Forest Engine), NumPy, Pandas
* **Frontend Design:** HTML5, CSS3 (Custom Stylesheets), Bootstrap 5, Chart.js
* **Data Serialization:** Pickle (.pkl)
* **Dataset Standard:** NSL-KDD Benchmarking Set

---

## 📂 Project Structure

```bash
AI-Enhanced-Intrusion-Detection-System/
│
├── Documentation/
│   └── Project_Documentation.docx
│
├── models/
│   ├── ids_model.pkl
│   └── scaler.pkl
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── alerts.html
│   └── about.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

## 💻 Setup & Local Deployment

### 1️⃣ Clone the Ecosystem Repository

```bash
git clone [https://github.com/spsourabh17/AI-Enhanced-Intrusion-Detection-System.git](https://github.com/spsourabh17/AI-Enhanced-Intrusion-Detection-System.git)
cd AI-Enhanced-Intrusion-Detection-System
```
2️⃣ Install Required Dependency Trees
```bash
pip install -r requirements.txt
```
3️⃣ Execute the Machine Learning Training Lifecycle
```bash
python train_model.py
```
4️⃣ Fire up the Enterprise Core Server
```bash
python app.py
```
## 🛣️ API Specifications & Routing

### Web Routes Matrix

| Interface Route | Allowed Methods | Functional Description |
| :--- | :--- | :--- |
| `/` | `GET` | Home screen featuring platform navigation and threat insights. |
| `/dashboard` | `GET` | Main monitoring terminal visualizing structural traffic stats. |
| `/predict` | `GET`, `POST` | Core interactive forms for feeding custom packet inputs. |
| `/alerts` | `GET` | Threat logging hub presenting continuous connection audits. |
| `/about` | `GET` | Comprehensive structural breakdown of the underlying data features. |

## 🖼️ Application Interfaces

* **🖥️ Home Screen:** Features a modern hero section introducing the platform capabilities, built-in metric badges, and interactive project cards.
* **📊 Live Analytics Dashboard:** Integrates **Chart.js** to render dynamic, real-time doughnut charts visualizing traffic distribution alongside running network log counters.
* **🔮 Feature Inspection Panel:** Provides a clean 10-field HTML input form pre-loaded with execution macros ("Simulate DoS", "Simulate R2L") for safe, on-demand payload testing.
* **🚨 Threat Log Ledger:** A structured administrative table tracking atomic incident timestamps, raw categorical detection labels, and multi-color precision confidence progress bars.

---

## 🔮 Planned Enhancements

* **🔌 Live Network Hooking:** Integrate raw frame sniffing components directly using `Scapy` to intercept physical socket streams.
* **🔑 RBAC Integration:** Implement comprehensive Role-Based Access Controls to restrict administrative dashboards.
* **🌐 Cloud Scaling:** Containerize with Docker for hosting on **AWS EC2** backed by a dedicated **Amazon RDS** tier.
* **🧠 Deep Learning Upgrade:** Construct an LSTM (Long Short-Term Memory) neural model layer to evaluate sequence-dependent connection vectors.

---

## 🔗 Project Resources

* 💻 Source Code Repository: [https://github.com/spsourabh17/ai-enhanced-intrusion-detection-system](https://github.com/spsourabh17/ai-enhanced-intrusion-detection-system)
* 🎥 Watch the Full Project Demo Video: [(https://drive.google.com/file/d/1Ze3ySLxm1GuyCuQ-IS7WIXZ4FZMlexUJ/view?usp=drive_link)](https://drive.google.com/file/d/1Ze3ySLxm1GuyCuQ-IS7WIXZ4FZMlexUJ/view?usp=drive_link)

---

## 👨‍💻 Author

**Sourabh Patil**

* 🔗 GitHub: [https://github.com/spsourabh17](https://github.com/spsourabh17)
* 💼 LinkedIn: [https://www.linkedin.com/in/sourabh-patil-5242402b7](https://www.linkedin.com/in/sourabh-patil-5242402b7)

---

## ⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub!
 
