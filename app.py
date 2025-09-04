from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder="frontend", static_folder="static")

# Load your trained Logistic Regression pipeline
with open("models/model.pkl", "rb") as f:
    lr_model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
  
    # Show the front-end
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        text = (data.get("text") or "").strip()

        if not text:
            return jsonify({"ok": False, "error": "No review text provided"}), 400

        # Since you saved the full pipeline (TF-IDF + Logistic Regression),
        # you can call predict_proba directly
        proba = lr_model.predict_proba([text])[0][1]  # probability of positive
        label = "positive" if proba >= 0.5 else "negative"

        return jsonify({
            "ok": True,
            "label": label,
            "prob_positive": float(proba)
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
