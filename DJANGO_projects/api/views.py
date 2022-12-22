from django.shortcuts import render
import collections

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SymbolDelete
from .serializers import SymbolDeleteSerializer
from drf_spectacular.utils import extend_schema
from symbol_delete.func import symbol_delete
# Create your views here.


class SymbolDeleteView(APIView):
    @extend_schema(request=SymbolDeleteSerializer, responses=SymbolDeleteSerializer)
    def get(self, request, s):
        ss = symbol_delete(s)
        symbol = SymbolDelete(ss)
        serializer = SymbolDeleteSerializer(instance=symbol)
        return Response(serializer.data)