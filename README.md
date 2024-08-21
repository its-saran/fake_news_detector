# Fake News Detection App

A simple Streamlit-based web application that predicts whether a piece of news is legitimate or fake. The model uses a pre-trained machine learning pipeline to make predictions based on user input.

## Features

- **Text Input:** Users can input news text into the app.
- **Character Count:** The app displays the number of characters in the input text.
- **Prediction:** The app predicts whether the news is "Legit" or "Fake" when the user clicks the "Check" button.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/fake-news-detection-app.git
cd fake-news-detection-app
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Running the App

To start the web application, run:

```bash
streamlit run app.py
```

This will launch a local web server and open the app in your default web browser.

## Usage
- Open the app in your browser.
- Enter the news text in the text area provided.
- Click the "Check" button to see the prediction. 
- The app will display whether the news is "Legit" or "Fake" in a header colored blue or red, respectively.