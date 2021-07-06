from rest_framework import serializers
from .models import Person
from datetime import datetime, timedelta, tzinfo

class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        today_date = datetime.today()
        birthday = datetime.strptime(obj.iin[0:6], "%y%m%d")
        age = int((today_date - birthday).days / 365.2425)
        return age

    def validate(self, data):
        """
        Check that the IIN is correct.
        """
        if not data['iin'].isnumeric() or len(data['iin']) > 12:
            raise serializers.ValidationError("Invalid input")
        return data
    
    class Meta: 
        model = Person
        fields = ('iin', 'age')
