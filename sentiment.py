import json
import boto3

def lambda_handler(event, context):
    comprehend = boto3.client(service_name="comprehend")
    text = event.get("text", None)
    payload = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    sentiment = payload["Sentiment"]
    
    return {
        'statusCode': 200,
        'body': json.dumps('Inference sentiment from this sentence'),
        'text': text,
        'sentiment': sentiment
    }