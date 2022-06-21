################
# Rodriguez, Maria de los Angeles - @AnGys09
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados
centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados
centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados y
retorne el resultado obtenido. Y viceversa.

def convertir_a_fahrrenheit(centigrados):
def convertir_a_centigrados(fahrenheit):
"""



def fahrenheit_a_celsius(f):
    """
    se hara la convercion de F° a C°
    """
    return (f-32)*(5.0/9.0)
    
f = float(input("ingrese los grados Fahrenhet   "))
c = fahrenheit_a_celsius(f)

print(f"los {f} grados Fahrenheit son {c} grados celsius")

def celsius_a_fahrenheit(c):
    """
    se hara la convercion de C° a F°
    """ 
    return (c*9.0/5.0)+32

c = float(input("Ingrese los Centigrados   "))

f = celsius_a_fahrenheit(c)
print(f"los {c} grados centigrados son {f} grados farenheit")