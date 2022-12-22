from django.db import models
import re

# Create your models here.
class SymbolDelete:
    def __init__(self, input):
        self.input = input
        self.result = self.symbol_delete(input)

    def symbol_delete(self, s):
        # s=str(s)
        stroka = re.sub(r'[.,"\'-?:!;]', '', s)
        return stroka

