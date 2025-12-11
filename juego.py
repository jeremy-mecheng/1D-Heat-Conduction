import random

# Función para obtener la retroalimentación (números correctos en la posición correcta y incorrecta)
def obtener_retroalimentacion(guess, secreto):
    correctos_posicion = 0
    correctos_incorrecta_pos = 0
    
    guess = list(str(guess))
    secreto = list(str(secreto))
    
    # Contar números correctos en posición correcta
    for i in range(4):
        if guess[i] == secreto[i]:
            correctos_posicion += 1
            guess[i] = secreto[i] = None  # Marcamos estos números como "ya comprobados"
    
    # Contar números correctos pero en posición incorrecta
    for i in range(4):
        if guess[i] is not None and guess[i] in secreto:
            correctos_incorrecta_pos += 1
            secreto[secreto.index(guess[i])] = None  # Eliminamos ese número de las posibles coincidencias
    
    return correctos_posicion, correctos_incorrecta_pos

# Función para generar todas las combinaciones posibles de 4 cifras
def generar_posibilidades():
    return [str(i).zfill(4) for i in range(1000, 10000)]

# Función para hacer un intento inteligente
def adivinar_numero():
    # El número secreto lo define el jugador, en una partida real se ingresaría aquí
    secreto = random.randint(1000, 9999)
    
    # Lista de todas las combinaciones posibles
    posibilidades = generar_posibilidades()
    
    intentos = 0
    while True:
        intentos += 1
        
        # El algoritmo hace una suposición (puede ser aleatoria o más lógica)
        guess = random.choice(posibilidades)
        
        # Mostrar intento
        print(f"Intento {intentos}: {guess}")
        
        # Obtener retroalimentación
        correctos_posicion, correctos_incorrecta_pos = obtener_retroalimentacion(guess, secreto)
        
        # Si la suposición es correcta
        if correctos_posicion == 4:
            print(f"¡Adivinado! El número es {guess}. Número de intentos: {intentos}")
            break
        
        # Filtrar las posibilidades basándonos en la retroalimentación
        posibilidades = [num for num in posibilidades if obtener_retroalimentacion(guess, int(num)) == (correctos_posicion, correctos_incorrecta_pos)]
        
        # Mostrar retroalimentación
        print(f"Retroalimentación: {correctos_posicion} en posición correcta, {correctos_incorrecta_pos} en posición incorrecta")
        
# Ejecutar el algoritmo
adivinar_numero()