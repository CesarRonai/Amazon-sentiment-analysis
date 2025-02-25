# Sentiment Analysis on Amazon Reviews

## 📌 Project Overview
This project aims to perform **Sentiment Analysis** on Amazon customer reviews using **Natural Language Processing (NLP)** and **Machine Learning** techniques. The final model is deployed as an API to predict the sentiment (positive or negative) of a given text input.

## 📂 Project Structure
```
Amazon Reviews Mega-Scale Analysis/
│-- api/              # API Flask for model inference
│-- data/             # Dataset used for training
│-- models/           # Saved models (.pkl)
│-- notebooks/        # Jupyter Notebooks with analysis and training steps
│-- sentiment_model.pkl    # Trained sentiment analysis model
│-- tfidf_vectorizer.pkl   # TF-IDF vectorizer for text transformation
│-- requirements.txt  # List of dependencies
│-- README.md         # Project documentation
```

## 🛠️ Installation and Setup
### 1️⃣ Clone the repository
```bash
git https://github.com/CesarRonai/Amazon-sentiment-analysis
cd your-repository
```
### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the API
### Start the Flask API locally
```bash
python api/app.py
```
### Example API request (using `curl`)
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"review": "I love this product!"}'
```
Expected Response:
```json
{"sentiment": "positive"}
```

## 🏗️ Model Training Pipeline
1. **Data Preprocessing**: Cleaning text, removing stopwords, and tokenization.
2. **Feature Extraction**: TF-IDF vectorization to convert text into numerical format.
3. **Model Training**: A `RandomForestClassifier` is trained for sentiment classification.
4. **Model Evaluation**: Metrics such as accuracy and classification report are used for performance evaluation.
5. **Deployment**: The trained model and TF-IDF vectorizer are saved as `.pkl` files and used in a Flask API.

## 📊 Results
- Achieved an accuracy of **XX%** on the test dataset.
- The model performs well in distinguishing between positive and negative reviews.

## 📌 Future Improvements
- Implement deep learning models such as **LSTMs** or **BERT** for improved accuracy.
- Deploy the API on a cloud service like **AWS** or **Google Cloud**.
- Build a **frontend interface** to interact with the model.

## 📝 License
This project is under the **MIT License**.

## 🙌 Contributing
Feel free to submit issues or pull requests to improve this project.

---
🔗 **Author:** [Cesar Ronai](https://www.linkedin.com/in/cesar-ronai-freitas-da-silva-8b2236149/)

