from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):
    ''''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, *args, **kwargs):
        ''''Returns a list of API view '''
        an_apiview = [
            'Uses HTTP methods as functions',
            'Is similar to a traditional django view',
            'most control',
            'reliable'
        ]
        return Response({'message' : 'hello', 'an_apiview' : an_apiview})

    def post(self, request, *args, **kwargs):
        ''''Create a hello message with your name'''

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            exp = serializer.validated_data.get('exp')
            salary = serializer.validated_data.get('salary')
            message = f'hello {name}, your salary is {salary} at experience {exp}'
            return Response({'message' : message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, **kwargs):
        # instance = self.get_object(id)
        # serializer = self.serializer_class(instance, data=request.data)
        # if serializer.is_valid():
        return Response({ 'method' : 'put'})

    def patch(self, request, pk=None, **kwargs):
        # instance = self.get_object(id)
        # serializer = self.serializer_class(instance, data=request.data)
        # if serializer.is_valid():
        return Response({ 'method' : 'patch'})

    def delete(self, request, pk=None, **kwargs):
        # instance = self.get_object(id)
        # serializer = self.serializer_class(instance, data=request.data)
        # if serializer.is_valid():
        return Response({ 'method' : 'delete'})

