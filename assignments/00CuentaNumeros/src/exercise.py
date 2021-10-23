from matplotlib import pyplot as pyplot
def grafica():
    #Código de la gráfica
    with open('/workspace/evidencia-integrador-/assignments/00CuentaNumeros/src/grafica evidencia integrador.csv', 'p') as juegos:
    
    juegos = ["PUBG", "Minecraft", "Pac-man", "Among us", "Tetris", "Fortnite", "League of legends", "Warzone", "World of warcraft"]
    numero_de_usuarios = [1037, 600, 505, 500, 500, 350, 101, 100, 100]

    plt.bar(juegos, numero_de_usuarios, width=0.7)

    plt.ylabel("numero de usuarios (en millones)")
    plt.xlabel("Nivel de fama de los juegos")

    plt.savefig("grafica_barras.jpeg")
    plt.show()

def main():
    #escribe tu código abajo de esta línea
    print("Este es un programa diseñado para aquellos que les gustan los videojuegos.")
    print("Aquí encontraras recomendaciones que te puedan interesar...")
    print('------------------------------------------------------------------------------')
    a=input("Enter para continuar: ")
    print('------------------------------------------------------------------------------')

    print('¡Hola usuario!')

    b=input('¿Te gustan los videojuegos? (si/no): ')
    print('\n')

    if b == 'no':
        print('Lamentamos no poder ayudarte. Adiós')
    
    
    elif b == 'si':
         
        test_list = ["PUBG", "Minecraft", "Pac-man", "Amongus", "Tetris", "Fortnite", "League-of-Leguends", "Warzone", "World-of-warcraft"] 
        print('En esta lista te mostramos los juegos mas famosos del 2021:')
        for i in range(len(test_list)): 
            
            print(test_list[i])
    else:
        print('Respuesta inválida')

    print('¿Te gustaria conocer dependiendo la categoria?(si/no)')
    d=input('')
    if d == 'si':
        #Opciones de las categorias
        print('¿Que categoria de juegos te gustaria conocer?')
        c= int(input('1:accion, 2:deportes, 3:aventura, 4: de rol: '))
    
        #Listas realizadas con for
        if c == 1:
            print('aqui estan unas sugerencias de juegos de accion mas populares hoy: ')
            lista_accion=['Call of Duty: Warzone','Fornite','Counter Strike: Global Offensive','Apex Legends']
            for i in range(len(lista_accion)): 
            
                print(lista_accion[i])

        elif c == 2:
            print('aqui estan unas sugerencias de juegos de deportes mas populares hoy: ')
            lista_deportes=['Fifa 22','NBA 2k22','Maddden NFL 18']
            for i in range(len(lista_deportes)): 
            
                print(lista_deportes[i])

        elif c == 3:
            print('aqui estan unas sugerencias de juegos de aventura mas populares hoy: ')
            lista_aventura=['it takes two','God of War','Monster Hunter: Rise','Hitman 3']
            for i in range(len(lista_aventura)): 
            
                print(lista_aventura[i])
        
        elif c == 4:
            print('aqui unas sugerencias de juegos de rol mas populares hoy: ')
            lista_rol=['Pilars of Eternity','Tales of...','Mas Effect Trilogy']
            for i in range(len(lista_rol)): 
            
                print(lista_rol[i])
        
        else:
            print('Respuesta inválida')
    elif d == 'no':
        print('Entonces...')
       
    else:
        print('Opcion Invalida')
        

    print('¿Te gustaria conocer cuales son los dispositivos mas utilizados para jugar?(si/no)')
    e=input('')

    #Primer informe con datos numericos
    if e == 'si':
        print('El primer lugar, sorprendentemente lo ocupan los dispositivos moviles ocupando un 49%.')
        print('En segundo lugar tenemos a los ordenadores, estos se hn popularizado mas en los ultimos años')
        print('debido a su gran capacidad que tiene, ocupa un 38%.')
        print('En tercer lugar se encuentran las videoconsolas, estos conforme pasa el tiempo se ha perdido')
        print('la comunidad, lo cual si comparamos con otros dispositivos, es el unico cuya unica funcion es jugar videojuegos,')
        print('estas ocupan tan solo un 30%')
        print('En cuarto lugar estan las tablets con un 26%')
        print('En quinto lugar se encuentran las consolas portatiles, que a pesar de su gran popularidad en años')
        print('anteriores, estos conforme pasan los años, se innovan cada vez menos y tienen menor capacidad por lo que')
        print('solamente lo utiliza un 17%.')
    elif e == 'no':
        print('De seguro esto te interesara')
    else:
        print('Respuesta invalida')
        print('¿Te gustaria conocer cuales son los dispositivos mas utilizados para jugar?(si/no)')
        e=input('')
    
    print ('¿Te interesa saber sobre las consolas recientes mas vendidas este 2021?(si/no)')
    w=input('')
    #Segundo informe con datos numericos
    if w == 'si':
        print('1- Ocupando el 58.6% se encuentra la consola mas reciente desarrollda por ninteno, la nintendo switch')
        print('2- En el segundo puesto se encuentra la playstation 5 desarrollada por sony con un 28.3%')
        print('3- En tercer y ultimo lugar se encuentra la xbox series x/s ocupando un 13.1% en el mercado ')
    elif w == 'no':
        print('Entonces...')
    else:
        print('Respuesta invalida')
    
            
    print('¿Te gustaria comprar alguna consola de videojuegos?')
    f=input('')
    if f == 'si':
        print('¿Cual es tu presupuesto?')
        g=int(input(''))
        
        if 2000< g <= 7000 :
            print('Hoy en dia tu presupuesto es algo bajo considernado los precios existentes, te recomendamos')
            print('buscar consolas de segunda mano, solo procura probarlo antes de pagar.')
        elif 13000> g >7000:
            print('Tu presupuesto es bueno, sin embargo, no esperes mucho potencial por lo que te recomiendo')
            print('la nintendo switch, de seguro te gustara.')
        elif 13000 <= g <20000:
            print('Tu presupuesto es bastante bueno, con ese dinero podras comprarte una consola de ultimo modelo')
            print('como la xbox series x, o la playstation 5!')
        elif g>=20000:
            print('Wow con ese dinero puedes comprarte la consola que tu quieras, hasta mas de una de ultimo modelo!!!.')
        elif g < 0:
            print('Me parece que lo que necesitas es pagar tus deudas :(')
        elif 0<=g<=2000:
            print('Es dificil encontrar una consola a tan buen precio')
        else:
            print('Respuesta invalida')
    elif f == 'no':
        print('Adios!')
    else:
        print('Respuesta invalida')

    

if __name__=='__main__':
    main()
