#juego ahorcado

def ahorcado ():

    palabra_oculta = "depresion"

    adivinanza = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    #esto se puede realizar así-> adivinanza = [_] * len(palabra_oculta)

    intentos = 6

    #creo un bucle que diga que mientra intentos sea mayor que 0
    #y "_" siga en adivinanza

    while intentos > 0 and "_" in adivinanza:
        letra = input("elige letra: ")

        #for i in range(len(palabra_oculta)):: Este bucle for itera sobre los índices de la palabra oculta.
        #range(len(palabra_oculta)) crea una secuencia de números desde 0 hasta el tamaño de la palabra oculta menos 1.
        #En cada iteración, i toma el valor de uno de esos índices.

        if letra in palabra_oculta:

            for i in range(len(palabra_oculta)):

                if palabra_oculta[i] == letra:
                    adivinanza[i] = letra

            print("acertaste gorfo")

        else:
            intentos -= 1

            #con f delante del print puedo usar {} para mostrar el numero de intentos
            print(f"perdiste una vida gorfo, te quedan {intentos} intentos")

        #"Adivinanza actual:": Esto es simplemente una cadena de texto que se imprime antes de mostrar la adivinanza actual.
        #Sirve como una especie de encabezado para que el jugador sepa qué está viendo.

        #" ".join(adivinanza): Aquí se está utilizando el método join de las cadenas de Python.
        #El método join toma una lista de cadenas y las une en una sola cadena, utilizando la cadena en la que se llama como separador.
        #En este caso, adivinanza es una lista de caracteres que representan la adivinanza actual.
        #La cadena vacía " " se utiliza como separador, lo que significa que cada elemento de la lista se separará por un espacio en la cadena resultante.
        print("Adivinanza actual:", " ".join(adivinanza))

    #fin del juego (el usuario ha ganado)

    if intentos == 0:
        print("perdiste boludo")

    if "_" not in adivinanza:
        print("ganaste malparido")

ahorcado()

