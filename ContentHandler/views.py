from textblob import TextBlob
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DetactLanguageSerializer
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
@api_view(['POST'])
def detect_language(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = DetactLanguageSerializer(data=request.data)
        if serializer.is_valid():
            text=serializer.data['text']
            text = TextBlob(text)
            lang= text.detect_language()
            with open('ContentHandler/language.json') as f:
                data = json.load(f)
                f.close()
                lang=data[lang]
            return Response(lang, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
