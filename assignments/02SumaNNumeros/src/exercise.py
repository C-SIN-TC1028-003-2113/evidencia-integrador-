def sumaNNumeros(n):
    suma = 0

    for i in range(1,n+1):
        suma = suma + i
    
    return suma

def main():
    #escribe tu código abajo de esta línea

    n = int(input("Dame un número:"))

    suma = sumaNNumeros(n)

    print(suma)
    
    
if __name__=='__main__':
    main()
