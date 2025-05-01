import pickle
import argparse
import re

# Load model and vectorizer
with open('model/phishing_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# Clean the input text (same as used during training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s:/.-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# CLI argument handling
parser = argparse.ArgumentParser(description="JA-PED: Just Another Phishing Email Detector")
parser.add_argument('--verbose', action='store_true', help='Show prediction explanation')
parser.add_argument('--strict', action='store_true', help='Use stricter detection threshold')
parser.add_argument('--save', action='store_true', help='Save the prediction result to output.txt')

args = parser.parse_args()

# Input from user
print("\nWelcome to JA-PED (Just Another Phising Email Detector!\n")
print("\n-------------------------------------------------------\n")
print("\nPlease paste your email content below:\n")

user_input = input("> ")

# Preprocess and predict
cleaned = clean_text(user_input)
X_vec = vectorizer.transform([cleaned])
prob = model.predict_proba(X_vec)[0][1]  # probability of being phishing

# Adjust threshold for strict mode
threshold = 0.5
if args.strict:
    threshold = 0.35  # more sensitive to phishing

result = "🚨 Phishing Email" if prob >= threshold else "🟢 Safe Email"

# Output
print("\n-------------------------------------------------------\n")
print(f"\n Prediction: {result}")

if args.verbose:
    print(f"Probability of phishing: {prob:.2f}")
    print(f"Threshold used: {threshold}")

if args.save:
    with open("output.txt", "w") as f:
        f.write(f"Prediction: {result}\n")
        f.write(f"Probability: {prob:.2f}\n")
    print("Prediction saved to output.txt")
