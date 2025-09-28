juegos = []


def add_game():  
    print("---Agregar juego---")
    nom=input("ingrese nombre del juego: ") # Usar input() para datos
    gen=input("ingrese genero del juego: ")
    New=(nom,gen,False)# Crear tupla (nombre, genero, False)
    juegos.append(New)# Usar append() en lista
    print("el juego se ingesado con exito")


def view_games():
        print("---Tu Colección---")
        if juegos:# Usar if not para verificar lista vacía
             for i, (nombre,genero,jugado) in enumerate(juegos):# Usar for con enumerate()
              estado = "✓" if jugado else "✗"
              print(f"{i+1}: {nombre} ({genero}) [{estado}]")# Desempaquetar tupla
        else :
            print("no hay juegos")


def complete_game():
    print("----Juegos Completados y Por Completar----")
    if juegos:
          
          for i, (nombre,genero,jugado) in enumerate(juegos):
              estado = "✓" if jugado else "✗"
              print(f"{i+1}: {nombre} ({genero}) [{estado}]")
          i=int(input("ingrese el numero del juego para marcarlo como completado: "))
          i=i-1

          if 0<= i <= len(juegos) :
              nombre,genero,jugado= juegos[i]
              juegos[i]= (nombre,genero,True)
              print(f"✅ {nombre} ha sido completado exitosamente")
            
          else :
              print("error intente de nuevo")
              complete_game()


    else :
        print("no hay juegos")

   
   
    # Usar if not para lista vacía
    # Usar >= y <= para validar índice
    # Modificar tupla en lista
    

def show_stats():
    
    if not juegos:
        print("No hay juegos en la colección.")
        return
    
    total = len(juegos)
    completados = 0
    
    for juego in juegos:
        if juego[2]:  # Si está completado
            completados += 1
    
    pendientes = total - completados
    
    print("=== ESTADÍSTICAS ===")
    print(f"Total de juegos: {total}")
    print(f"Completados: {completados}")
    print(f"Pendientes: {pendientes}")


