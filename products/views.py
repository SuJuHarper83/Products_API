from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
# As a developer, I want to create a GET endpoint the responds with a 200 success status code and 
# all of the products within the Product table.

# As a developer, I want to create a GET by id endpoint that does the following things:
# · Accepts a value from the request’s URL (The id of the product to retrieve).
# · Returns a 200 status code.
# · Responds with the product in the database that has the id that was sent through the URL.

# As a developer, I want to create a POST endpoint that does the following things:
# · Accepts a body object from the request in the form of a Product model.
# · Adds the new product to the database.
# · Returns a 201 status code.
# · Responds with the newly created product object.

@api_view (['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# As a developer, I want to create a PUT endpoint that does the following things:
# · Accepts a value from the request’s URL (The id of the product to be updated).
# · Accepts a body object from the request in the form of a Product model.
# · Finds the product in the Product table and updates that product with the properties that were sent in the request’s body.
# · Returns a 200 status code.
# · Responds with the newly updated product object.

# As a developer, I want to create a DELETE endpoint that does the following things:
# · Accepts a value from the request’s URL.
# · Returns a 204 status code (NO CONTENT).

@api_view (['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(Product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# As a developer, I want to use Postman to make a POST, PUT, DELETE, and both GET requests 
# (get by id and get all) request to my REST web API, save it to a collection, and 
# then export it as a JSON from Postman.
