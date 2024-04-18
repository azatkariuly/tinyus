from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# Create your views here.
@api_view(['POST'])
def handleRequest(request):
    print(list(request.data.items()))

    print('parentId', request.data.get('parentId'))

    print('child', request.data.get('childInputTime'))

    return Response({"result": "done"})