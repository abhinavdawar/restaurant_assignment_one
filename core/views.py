import json
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Product
from core.serializers import ProductSerializer, OrderSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.core.serializers import serialize


class CoreViewSet(viewsets.ModelViewSet):

    @action(methods=["GET"], detail=False, url_path="product-list")
    def list_all_products(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = json.loads(serialize('json', products))
        return Response(
            data=data,
            status=HTTP_200_OK
        )
        # return render(request, 'core/view_products_template.html', {'articles': products})

    @action(methods=["POST"], url_path="create-order", detail=False)
    def create_orders(self, request, *args, **kwargs):
        data = request.data
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data="New Order has been created",
            status=HTTP_201_CREATED
        )
    