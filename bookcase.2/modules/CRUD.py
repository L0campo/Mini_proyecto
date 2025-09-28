

libros= []




def agregarLibro():
    print("====== Agregar nuevo Libro 📔 ======")
    ti=input("Digite el Titulo del libro: ")
    au=input("Digite el nombre del autor del libro: ")
    gen=input("Digite el genero del libro: ")
    año=int(input("Digite el año de publicacion del libro: "))
    estado=input("el libro a sido leido? (s/n): ").lower()
    
    if estado == "s":
        estado=True
    
    elif estado == "n":
        estado=False

    else :
        print("⚠️ seleccione una opcion valida ⚠️")

    New=[ti,au,gen,año,estado]
    libros.append(New)

    print("El libro fue agregado con exito ✅")

def leerBiblioteca():
    print("====== Biblioteca 📚 ======".center(50))

    if libros:

        for i, libro in enumerate(libros):
            titulo = libro[0]
            nombre = libro[1]      
            genero = libro[2]      
            año = libro[3]  
            leido = libro [4]    
            estado = "✓" if leido else "✗"
            print(f"{i+1}. titulo: {titulo} | nombre: {nombre} | genero: {genero} | año: {año} | Estado: {estado} | ")
            

    else :
        print("no hay libros en la biblioteca")


def buscadorMenu():
    print("====== Buscador de libros 🔎 ======".center(50))
    print(" escoja una opcion del 1-3 para buscar el libro que deseas")




def buscarlibros(palabra,n):
    sugerencias = []
    
    
    
    
    for libro in libros:
        titulo, autor, genero, _, _ = libro
        
        if n==1:
            if palabra.lower() in titulo.lower() :
               sugerencias.append(libro)
        
        elif n==2:
         
            if palabra.lower() in autor.lower() :
               sugerencias.append(libro)
          
        elif n==3:
            
            if palabra.lower() in genero.lower():
               sugerencias.append(libro)
            
            
            
        else :
            print("error")  
            
            
            
            
            
            sugerencias.append(libro)
    return sugerencias

def estadoLibro():
    leerBiblioteca()

    num=int(input("ingrese el numero del libro que desea marcar como leido: "))
    num= num - 1

    if 0<= num < len(libros):

        libros[num][4]= not libros[num][4]
        estado ="✓" if libros[num][4] else "✗"
        print(f"✅ el cambio fue completado con exitosamente")
    

    
    else :
        print("error intente de nuevo")

def estadisticasLibros():
    
    leidos=0
    porleer=0
    total=len(libros)
    generos = {}

    for libro in libros:

        if libro[4] == False:
            porleer += 1

        else :
            leidos += 1
            
                   
        genero = libro[2]

        if genero in generos:
            generos[genero] += 1
        else :
            generos[genero] = 1
                
    if generos:
        generoMasFrecuente = max(generos, key=generos.get)
    else:
        generoMasFrecuente = "No hay géneros disponibles"

    print("===== Estadísticas 📊 =====")
    print(f"Total de libros: {total}")
    print(f"Leídos: {leidos}")
    print(f"Por leer: {porleer}")   
    print(f"Género más frecuente: {generoMasFrecuente} ")
    
        

def eliminarLibro():
      
    leerBiblioteca()
    
    print("====== Eliminar libros🗑️ =======".center(50))

    eliminar=int(input("ingrese el numero del libro que desea eliminar: "))

    libro = libros.pop(eliminar-1)
    
    print(f"se elimino el libro {libro[0]}")


