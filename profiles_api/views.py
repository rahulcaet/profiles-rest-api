from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    ''''Test API View'''

    def get(self, request, *args, **kwargs):
        ''''Returns a list of API view '''
        an_apiview = [
            'Uses HTTP methods as functions',
            'Is similar to a traditional django view',
            'most control',
            'reliable'
        ]
        return Response({'message' : 'hello', 'an_apiview' : an_apiview})


