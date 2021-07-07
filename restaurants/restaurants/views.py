from rest_framework import status
from rest_framework.views import APIView
from .serializers import RestaurantSerializer, PizzaSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from .models import Restaurant, Pizza


class listRestaurants(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    def get(self, request):
        restaurants = Restaurant.objects.all()
        return Response(RestaurantSerializer(restaurants, many=True).data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class restaurantDetail(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    def get_object(self, id):
        return Restaurant.objects.get(id = id)

    def get(self, request, id):
        restaurant = self.get_object(id = id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    def put(self, request, id):
        restaurant = self.get_object(id = id)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        restaurant = self.get_object(id = id)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant = self.get_object(id = id)
        if restaurant is not None:
            restaurant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Not found"}, status=status.HTTP_400_BAD_REQUEST)

class listPizzas(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    def get(self, request):
        pizzas = Pizza.objects.all()
        return Response(PizzaSerializer(pizzas, many=True).data)

    def post(self, request):
        serializer = PizzaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class pizzaDetail(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    def get_object(self, id):
        return Pizza.objects.get(id = id)

    def get(self, request, id):
        pizza = self.get_object(id = id)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)
    
    def put(self, request, id):
        pizza = self.get_object(id = id)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        pizza = self.get_object(id = id)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pizza = self.get_object(id = id)
        if pizza is not None:
            pizza.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Not found"}, status=status.HTTP_400_BAD_REQUEST)