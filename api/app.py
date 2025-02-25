from flask import Flask, request, jsonify
import joblib

# Carregar o modelo e o vetorizador TF-IDF
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Criar a API Flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review_text = data.get("review", "")

    # Vetorizar o texto recebido
    review_vector = vectorizer.transform([review_text])

    # Fazer a previsão
    prediction = model.predict(review_vector)[0]

    # Retornar a classe
    result = {"sentiment": "positivo" if prediction == 1 else "negativo"}
    return jsonify(result)

# Rodar a API
if __name__ == "__main__":
    app.run(debug=True)
