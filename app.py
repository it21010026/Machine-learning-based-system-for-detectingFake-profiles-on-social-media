from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('fake_profile_predictor.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from form
    profile_data = {
        'username': [request.form['username']],
        'email': [request.form['email']],
        'age': [int(request.form['age'])],
        'gender': [request.form['gender']],
        'location': [request.form['location']],
        'occupation': [request.form['occupation']],
        'followers': [int(request.form['followers'])],
        'posts': [int(request.form['posts'])]
    }

    # Convert user input to DataFrame
    input_df = pd.DataFrame(profile_data)

    # Get prediction probabilities
    prediction_proba = model.predict_proba(input_df)

    # Generate a descriptive report
    fake_probability = prediction_proba[0][1] * 100
    result = f"The input profile data is as follows: Username: {profile_data['username'][0]}, Email: {profile_data['email'][0]}, Age: {profile_data['age'][0]}, Gender: {profile_data['gender'][0]}, Location: {profile_data['location'][0]}, Occupation: {profile_data['occupation'][0]}, Followers: {profile_data['followers'][0]}, and Posts: {profile_data['posts'][0]}. Based on the trained model, there is a {fake_probability:.2f}% probability that the profile is fake."

    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
