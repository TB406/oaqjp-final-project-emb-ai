import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  # Check for empty or blank input
        return None
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictor = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictor, key = emotion_predictor.get)
        return {
            'anger': emotion_predictor['anger'],
            'disgust': emotion_predictor['disgust'],
            'fear': emotion_predictor['fear'],
            'joy': emotion_predictor['joy'],
            'sadness': emotion_predictor['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return None

