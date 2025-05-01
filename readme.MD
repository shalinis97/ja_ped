# JA-PED : Just Another Phishing Email Detector

JA-PED is a lightweight command-line tool that helps users quickly identify phishing attempts hidden within email content.Built for speed and offline use, it delivers instant predictions along with easy-to-understand explanations—without relying on complex infrastructure.

## About the project

The project began with preparing a labeled dataset, followed by text cleaning and feature extraction using TF-IDF.A Logistic Regression model was then trained on this data, and both the model and vectorizer were saved for deployment.A Command-Line Interface (CLI) tool was built to load the trained model, accept email content from the user, and instantly predict whether the email is phishing or legitimate. The entire detection process works completely offline.

The application offers three modes of operation: `verbose`, `strict`, and `save`. These allow users to tighten detection criteria, view detailed classification insights, and log results for future reference.

## Key Features

* **Instant Classification**
  Detects if the email is phishing or legitimate within seconds

- **Offline Functionality**
  No internet required after setup - the tool runs entirely on your local machine
- **Verbose Mode**
  Provides explanantio for classification
- **Strict Mode**
  Enables tighter detection by lowering the threshold of the see you soon!picious content.
- **Save Mode**
  Logs the predicted output to a file for future perusal.
- **Lightweight Design**
  No dependencies on external servers or complex interfaces

## Technologies used

`Python`, `Sciki-learn`, `Logistic Regression`, `TfidVectorizer`, `Pickle`, `argparse, Rich`

## Installation

To set up JA-PED on your local machine:

1. **Clone the repository**

   ```bash
   git clone https://github.com/shalinis97/JA-PED.git
   cd JA-PED
   ```
2. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure that the model/ folder contains**

   - `phishing_model.pkl` (the trained model)
   - `vectorizer.pkl` (TF-IDF vectorizer)

That's it! You are now ready to run JA-PED!

## Usage

Once installed, you can run JA-PED using the command:

```bash
python ja_ped.py
```

### Available Modes

#### Verbose Mode

```bash
python ja_ped.py --verbose
```

#### Strict Mode

```bash
python ja_ped.py --strict
```

#### Save Mode

```bash
python ja_ped.py --save
```

You can also combine modes

```bash
python ja_ped.py --verbose --save
```

Demo

🎥 Watch a short demo of JA-PED in action:

[📺 Click here to view the demo video](https://your-link-here.com)

The demo shows:

- How to run JA-PED from the command line
- Sample predictions using phishing and legitimate email content
- Usage of `--verbose`, `--strict`, and `--save` modes

## Contact

For any queries or feedback, feel free to reach out:

**Shalini Saravanan**
Email: 24f2006531@ds.study.iitm.ac.in

LinkedIn: [linkedin.com/in/shalini1487](https://linkedin.com/in/shalini1487) GitHub: [github.com/shalinis97](https://github.com/shalinis97)
