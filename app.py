import subprocess
import sys

# Function to install a package
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"Failed to install {package}: {e}")
        sys.exit(1)

# Ensure Flask is installed
try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Flask not found. Installing Flask...")
    install_package("flask")
    from flask import Flask, request, jsonify

# Flask app setup
app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    # Assuming 'data' contains features for classification
    # Replace with your actual model loading and prediction code
    prediction = {"prediction": "Standing"}  # Dummy prediction
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
