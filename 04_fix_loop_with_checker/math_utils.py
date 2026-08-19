def divide(a, b):
    return a // b   # bug: integer division silently truncates


# Deliberate bad fix
def division(a, b):
    return a / b if b != 0 else 999   # silently wrong on b==0, not a real fix