# crop-yeild-prediction
# 🌾 Crop Yield Prediction using Machine Learning

## 📌 Overview
This project predicts **crop yield** using machine learning models trained on agricultural and environmental data.  
It takes inputs such as **NPK values, temperature, humidity, soil pH, and rainfall** to estimate yield in kg/ha.  
The model is deployed on **IBM Cloud Machine Learning** for real-time predictions.

---

## 🚀 Features
- Data preprocessing & cleaning
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Deployment on IBM Cloud ML Runtime
- Real-time prediction via API

---

## 📊 Dataset
- **File**: `100.csv`
- **Features**:
  - **N**: Nitrogen content in soil
  - **P**: Phosphorus content in soil
  - **K**: Potassium content in soil
  - **Temperature** (°C)
  - **Humidity** (%)
  - **pH** of soil
  - **Rainfall** (mm)
  - **Yield** (kg/ha) — Target variable

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **IBM Cloud Machine Learning**

---

## 📂 Project Structure
```
crop-yield-prediction/
│-- data/
│   └── 100.csv
│-- notebooks/
│   └── crop_yield_prediction.ipynb
│-- src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── predict.py
│-- results/
│   ├── model_metrics.png
│   └── crop_yield_model.pkl
│-- requirements.txt
│-- README.md
```

---

## ⚙️ Installation & Usage
```bash
git clone https://github.com/your-username/crop-yield-prediction.git
cd crop-yield-prediction
pip install -r requirements.txt
jupyter notebook notebooks/crop_yield_prediction.ipynb
```

---

## 🌐 Deployment
[IBM Cloud Deployment Link](https://au-syd.dai.cloud.ibm.com/ml-runtime/deployments/33ba00d0-832b-46f6-9ec5-59138713601c?space_id=255d875e-1b1b-450c-9bd6-136beb3b3c85&context=cpdaas)

---

## 📈 Results
- **Best Model**: Random Forest Regressor
- **R² Score**: Example value
- Example prediction:
  Input: N=90, P=40, K=40, Temp=25°C, Humidity=80%, pH=6.5, Rainfall=200mm  
  Output: Predicted yield = 2800 kg/ha

