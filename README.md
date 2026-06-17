#  Rainfall Prediction System

##  Project Overview
The Rainfall Prediction System is a Machine Learning-based web application that predicts whether rainfall is likely to occur based on various weather parameters. The project uses a trained machine learning model and provides predictions through an interactive Streamlit interface.

##  Features
- Predicts rainfall based on weather conditions
- Simple and user-friendly web interface
- Real-time prediction results
- Machine Learning model integration
- Data preprocessing and feature scaling

##  Technologies Used
- Python
- Machine Learning
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Pickle

##  Input Parameters
The model uses the following weather attributes:

- Day
- Pressure
- Maximum Temperature
- Temperature
- Minimum Temperature
- Dew Point
- Humidity
- Cloud Cover
- Sunshine
- Wind Direction
- Wind Speed

##  Project Structure

```text
Rainfall-Prediction-System/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── Rainfall.xlsx
├── Untitled0.ipynb
└── README.md
```

##  Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Rainfall-Prediction-System.git
```

### Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn openpyxl
```

### Run the Application

```bash
streamlit run app.py
```

##  How It Works

1. Enter the weather parameters.
2. Click the **Predict Rainfall** button.
3. The machine learning model processes the input data.
4. The system displays the prediction result.

##  Machine Learning Workflow

- Data Collection
- Data Preprocessing
- Feature Scaling
- Model Training
- Model Evaluation
- Deployment using Streamlit

##  Future Improvements

- Rainfall amount prediction
- Real-time weather API integration
- Advanced machine learning models
- Interactive weather dashboard

##  Author

**Nandani Rajput**

B.Tech (Computer Science Engineering)  
GLS University, Ahmedabad

Interested in Artificial Intelligence, Machine Learning, Data Science, and Data Analytics.

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.
