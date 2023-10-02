def rectangle(a, b):

    if not (isinstance(a, int)) or not (isinstance(b, int)):
        return "Enter valid values!"

    def area():
        return a*b

    def perimeter():
        return (a+b) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
