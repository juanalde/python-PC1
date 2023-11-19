num1 = float(input("Ingrese el primer número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)