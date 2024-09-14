def saludo():
    nombre = input("Bienvenido, cuál es su nombre: ")
    print("Hola " + nombre) 

def suma_numeros(a,b):
    suma = a + b
    return suma

if __name__=="__main__":
    saludo()
    print("La suma de 7 y 4 es: ")
    suma_numeros(7, 4)