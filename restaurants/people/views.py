from .models import Person
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import PersonSerializer

@api_view(['POST'])
def createPerson(request):
    """Get age by iin"""
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def personDetail(request, iin):
    """Get person by IIN"""
    person = Person.objects.get(iin = iin)
    serializer = PersonSerializer(person)
    if person is None:
        return Response({ "description": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
