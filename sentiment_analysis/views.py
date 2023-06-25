from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SentimentSerializer
from setfit import SetFitModel


@api_view(['POST'])
def analyze_sentiment(request):
    text = request.data.get('text')
    if text:
        model = SetFitModel.from_pretrained('StatsGary/setfit-ft-sentinent-eval')
        sentiment = model([text])[0]
        sentiment_mapping = {
            0: 'negative',
            1: 'neutral',
            2: 'positive'
        }
        sentiment_str = sentiment_mapping.get(sentiment.item(), 'unknown')
        response_data = {'sentiment': sentiment_str}
        return Response(response_data, status=200)
    return Response({'error': 'Invalid request'}, status=400)

# @api_view(['POST'])
# def analyze_sentiment(request):
#     text = request.data.get('text')
#     print(text)
#     if text:
#         model = SetFitModel.from_pretrained('StatsGary/setfit-ft-sentinent-eval')
#         sentiment = model([text])[0].item()   
#         print("Predicted sentiment:", sentiment)
#         serializer = SentimentSerializer(data={'text': text, 'sentiment': sentiment})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#     return Response({'error': 'Invalid request'}, status=400)
