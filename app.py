from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home1():
    return render_template("home.html")

@app.route("/voice")
def voice():
    return render_template("voice.html")
@app.route('/how')
def how():
    return render_template('how.html')


@app.route('/about')
def about1():
    return render_template('about.html')



@app.route('/index')
def about():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract input features from the form
        features = [float(x) for x in request.form.values()]
        data = np.array([features])
        prediction = model.predict(data)[0]
        result = "does NOT have heart disease" if prediction == 1 else "has heart disease"
        return render_template("predict.html", prediction_text=f"The patient {result}.")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
