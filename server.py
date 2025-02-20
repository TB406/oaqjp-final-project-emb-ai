# pylint: disable=consider-using-f-string
"""This module is the web deployment of the application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Function implements the emotion detector to analyse the text for emotion type"""
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return "The given text has been identified as {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    """Function pulls from the index file for web application format""" 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5054)
    