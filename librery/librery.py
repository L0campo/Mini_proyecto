usuarios = {}
libros = {}
generos_disponibles = set()

def registrar_usuario(usuarios, cedula, nombre, generos):
    if cedula in usuarios:
        print("❌ El usuario ya existe.")
        return
    usuarios[cedula] = {
        "nombre": nombre,
        "generos_favoritos": set(generos),
        "historial": []
    }
    generos_disponibles.update(generos)
    print(f"✅ Usuario {nombre} registrado con géneros favoritos: {generos}")

def agregar_libro(libros, codigo, titulo, autor, genero):
    if codigo in libros:
        print("❌ El código del libro ya existe.")
        return
    libros[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "disponible": True
    }
    generos_disponibles.add(genero)
    print(f"✅ Libro '{titulo}' agregado al catálogo.")

def prestar_libro(usuarios, libros, cedula, codigo):
    if cedula not in usuarios:
        print("❌ Usuario no registrado.")
        return
    if codigo not in libros:
        print("❌ Libro no encontrado en el catálogo.")
        return
    if not libros[codigo]["disponible"]:
        print("⚠️ El libro ya está prestado.")
        return
    libros[codigo]["disponible"] = False
    usuarios[cedula]["historial"].append(f"Prestado: {libros[codigo]['titulo']}")
    print(f"✅ {usuarios[cedula]['nombre']} ha prestado '{libros[codigo]['titulo']}'.")

def devolver_libro(usuarios, libros, cedula, codigo):
    if cedula not in usuarios or codigo not in libros:
        print("❌ Usuario o libro no encontrado.")
        return
    if libros[codigo]["disponible"]:
        print("⚠️ Este libro ya estaba disponible.")
        return
    libros[codigo]["disponible"] = True
    usuarios[cedula]["historial"].append(f"Devuelto: {libros[codigo]['titulo']}")
    print(f"✅ '{libros[codigo]['titulo']}' devuelto por {usuarios[cedula]['nombre']}.")

def recomendar_libros(usuarios, libros, cedula):
    if cedula not in usuarios:
        print("❌ Usuario no registrado.")
        return
    favoritos = usuarios[cedula]["generos_favoritos"]
    recomendaciones = [
        datos for datos in libros.values()
        if datos["genero"] in favoritos and datos["disponible"]
    ]
    print(f"\n📚 Recomendaciones para {usuarios[cedula]['nombre']}:")
    if recomendaciones:
        for libro in recomendaciones:
            print(f" - {libro['titulo']} ({libro['autor']}) [{libro['genero']}]")
    else:
        print("⚠️ No hay recomendaciones disponibles en este momento.")

def analisis_usuarios(usuarios, ced1, ced2):
    if ced1 not in usuarios or ced2 not in usuarios:
        print("❌ Uno de los usuarios no existe.")
        return
    g1 = usuarios[ced1]["generos_favoritos"]
    g2 = usuarios[ced2]["generos_favoritos"]

    print(f"\n📊 Análisis entre {usuarios[ced1]['nombre']} y {usuarios[ced2]['nombre']}:")
    print(" - Géneros en común:", g1 & g2)  # Intersección
    print(" - Géneros únicos:", g1 ^ g2)    # Diferencia simétrica
    print(f" - ¿{usuarios[ced1]['nombre']} es subconjunto de {usuarios[ced2]['nombre']}?:", g1 <= g2)
    print(f" - ¿{usuarios[ced2]['nombre']} es subconjunto de {usuarios[ced1]['nombre']}?:", g2 <= g1)

def generar_reporte(usuarios):
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return
    print("\n=== Reporte de Usuarios ===")
    for cedula, datos in usuarios.items():
        print(f"\n👤 {datos['nombre']} (Cédula: {cedula})")
        print(f" - Géneros favoritos: {datos['generos_favoritos']}")
        print(" - Historial:")
        if datos["historial"]:
            for mov in datos["historial"]:
                print(f"   • {mov}")
        else:
            print("   (Vacío)")



def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Registrar usuario")
        print("2. Agregar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Recomendar libros")
        print("6. Análisis de usuarios")
        print("7. Generar reportes")
        print("8. Ver catálogo de libros")
        print("9. Ver géneros disponibles")
        print("0. Salir")

        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            ced = input("Cédula: ")
            nombre = input("Nombre: ")
            generos = input("Géneros favoritos (separados por coma): ").split(",")
            generos = [g.strip() for g in generos]
            registrar_usuario(usuarios, ced, nombre, generos)

        elif opcion == "2":
            codigo = int(input("Código del libro: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            agregar_libro(libros, codigo, titulo, autor, genero)

        elif opcion == "3":
            ced = input("Cédula: ")
            codigo = int(input("Código del libro: "))
            prestar_libro(usuarios, libros, ced, codigo)

        elif opcion == "4":
            ced = input("Cédula: ")
            codigo = int(input("Código del libro: "))
            devolver_libro(usuarios, libros, ced, codigo)

        elif opcion == "5":
            ced = input("Cédula: ")
            recomendar_libros(usuarios, libros, ced)

        elif opcion == "6":
            ced1 = input("Cédula del primer usuario: ")
            ced2 = input("Cédula del segundo usuario: ")
            analisis_usuarios(usuarios, ced1, ced2)

        elif opcion == "7":
            generar_reporte(usuarios)

        elif opcion == "8":
            if libros:
                print("\n=== Catálogo de Libros ===")
                for cod, datos in libros.items():
                    estado = "✅ Disponible" if datos["disponible"] else "❌ Prestado"
                    print(f"{cod}: {datos['titulo']} - {datos['autor']} [{datos['genero']}] ({estado})")
            else:
                print("⚠️ No hay libros en el catálogo.")

        elif opcion == "9":
            print("📚 Géneros disponibles:", generos_disponibles if generos_disponibles else "Vacío")

        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

menu()