from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    ''''serializes a name field for testing our APIView'''
    name = serializers.CharField(max_length=10)
    exp = serializers.DecimalField(max_digits=4, decimal_places=2, max_value=60, min_value=2)
    salary = serializers.FloatField()

    def validate_name(self, value):
        ''''Check that the name field doesnt contain @ special character'''
        if '@' in value:
            raise serializers.ValidationError("name cant contain underscore in it {}".format(value))

        return value

    def validate(self, data):
        '''
        Check that salary is above threshold of age
        '''

        if data.get('salary') < 2 * data.get('exp') * 100000:
            raise serializers.ValidationError("salary has not passed threshold of experience level")
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    '''serializes a user profile model object'''
    password = serializers.CharField(write_only=True,
                                     style={ 'input_type' : 'password',
                                             'placeholder' : 'Password'})
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        # extra_kwargs = {
        #     'password' :  {
        #         'write_only' : True,
        #         #'style' : { 'input_type' : 'password'}
        #     }
        # }

    def create(self, validated_data):
        '''create a new user'''
        user = models.UserProfile.objects.create_user(
                    name=validated_data.get('name'),
                    email=validated_data.get('email'),
                    password=validated_data.get('password')
                   )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """"Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        #fields = '__all__'
        fields = ('íd', 'user_profile', 'status_text', 'created_at')
        extra_kwargs = { 'user_profile' : { 'read_only' : True }}
