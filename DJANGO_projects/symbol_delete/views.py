from django.shortcuts import render
from django.http import HttpResponse
from . import func
# Create your views here.

def index(request, s):
    return HttpResponse(f'Строка без знаков препинания: {func.symbol_delete(s)}')
