from rest_framework import serializers

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



