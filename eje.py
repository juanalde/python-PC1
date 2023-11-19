import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    # Verificamos la naturaleza de las soluciones
    if discriminante >= 0:
        # Soluciones reales
        solucion1 = (-b + math.sqrt(discriminante)) / (2*a)
        solucion2 = (-b - math.sqrt(discriminante)) / (2*a)
        return solucion1, solucion2
    else:
        # No hay solución real
        return None

# Solicitamos los coeficientes al usuario
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
c = float(input("Ingrese el coeficiente 'c': "))

# Calculamos las soluciones
soluciones = resolver_ecuacion_cuadratica(a, b, c)

# Mostramos las soluciones o un mensaje si no hay solución real
if soluciones is not None:
    print("Solución 1:", soluciones[0])
    print("Solución 2:", soluciones[1])
else:
    print("Ecuación no presenta solución real")