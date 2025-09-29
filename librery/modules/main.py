
import modules. utli as u
import modules.mesage as m
import modules.Crud as c

libros = c.libros


while True:
     m.menu()
     opcion = int(input("👉 Selecciona una opción: "))
     u.clear_screen()


     if opcion == 1:
            print("Registrar usuario")
            ced = input("Cédula: ")
            nombre = input("Nombre: ")
            generos = input("Géneros favoritos (separados por coma): ").split(",")
            generos = [g.strip() for g in generos]
            c.registrar_usuario(c.usuarios, ced, nombre, generos)
            u.clear_screen()

     elif opcion == 2:
            print("Agregar libro")
            codigo = int(input("Código del libro: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            c.agregar_libro(c.libros, codigo, titulo, autor, genero)
            u.clear_screen()

     elif opcion == 3:
            print("Prestar libro")
            ced = input("Cédula: ")
            codigo = int(input("Código del libro: "))
            c.prestar_libro(c.usuarios, c.libros, ced, codigo)
            u.clear_screen()

     elif opcion == 4:
            print("Devolver libro")
            ced = input("Cédula: ")
            codigo = int(input("Código del libro: "))
            c.devolver_libro(c.usuarios, c.libros, ced, codigo)
            u.clear_screen()

     elif opcion == 5:
            print("Recomendar libros")
            ced = input("Cédula: ")
            c.recomendar_libros(c.usuarios, c.libros, ced)
            u.clear_screen()

     elif opcion == 6:
            print("Análisis de usuarios")
            ced1 = input("Cédula del primer usuario: ")
            ced2 = input("Cédula del segundo usuario: ")
            c.analisis_usuarios(c.usuarios, ced1, ced2)
            u.clear_screen()

     elif opcion == 7:
            print("Generar reportes")
            c.generar_reporte(c.usuarios)
            u.clear_screen()

     elif opcion == 8:
            print("Ver catálogo de libros")
            c.catalogo()
            
            u.pasuar
            u.clear_screen()

     elif opcion == 9:
            print("Ver géneros disponibles")
            print("📚 Géneros disponibles:", c.generos_disponibles if c.generos_disponibles else "Vacío")
            u.clear_screen()

     elif opcion == 0:
            print("👋 Saliendo del sistema...")
            u.clear_screen()
            break

     else:
            print("❌ Opción no válida. Intenta de nuevo.")
            u.pasuar()
            u.clear_screen()