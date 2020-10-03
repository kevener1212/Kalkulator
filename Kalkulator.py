print("kalkulator")
a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
z = input("Jakiego typu dzialanie chcesz wykonac(+,-,*,/,**)")

Znaki = {"+": a + b, "-": a - b, "*": a * b, "/": a / b, "**": a ** b}

if z == "+":
    print(Znaki["+"])
elif z == "-":
    print(Znaki["-"])
elif z == "":
    print(Znaki["*"])
elif z == "/":
    print(Znaki["/"])
elif z == "**":
    print(Znaki["**"])
else:
    print("nie znaleziono znaku (upewnij sie ze uzyles dobrego znaku)")

