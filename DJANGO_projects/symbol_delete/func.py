import re


def symbol_delete(s):
    # s=str(s)
    stroka = re.sub(r'[.,"\'-?:!;]', '', s)
    return stroka