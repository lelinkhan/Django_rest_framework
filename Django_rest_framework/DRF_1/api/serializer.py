from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) #one object restriction

    # validators
    def start_with_r(value):
        if value[0].lower() != 'l':
            raise serializers.ValidationError('name must be start with R')
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

        # read_only_fields = ['name','roll'] # multiple object restriction
        # extra_kwargs = {'name':{'read_only':True}}

        # field level validation
    def validate_roll(self,value):
        if value >= 1000:
            raise serializers.ValidationError('Seat Full')
        return value

    # object level validation

    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'lelin' and ct.lower() != 'natore':
            raise serializers.ValidationError('City should be must Natore')
        return data
