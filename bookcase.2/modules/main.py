
import modules. utli as u
import modules.mesage as m
import modules.CRUD as c



isActive=True


while isActive:
    m.menu()
    try: 
        opcion=int(input("digite una opcion del 1-7: "))
        u.clear_screen()
        match opcion:

            case 1:
                c.agregarLibro()
                u.pasuar()
                u.clear_screen()

            case 2:
                
                c.leerBiblioteca()
                u.pasuar()
                u.clear_screen()

            case 3:
                
                c.buscadorMenu()
                n=int(input("Titulo 1. / Autor2. / Genero3.: "))
                entrada = input("\n🔎 digite una palabra para empezar la busqueda: ")
                resultados = c.buscarlibros(entrada,n)
                if resultados:
                    print("\n📚 Resultados encontrados:")
                    for i, libro in enumerate(resultados, 1):
                        print(f"{i}. titulo: {libro[0]} | Autor: {libro[1]} | Genero: {libro[2]}")
                else:
                    print("❌ No se encontraron coincidencias.")
                u.pasuar()
                u.clear_screen()

            case 4:
                
                c.estadoLibro()
                u.pasuar()
                u.clear_screen()

            case 5:
                
                c.estadisticasLibros()
                u.pasuar()
                u.clear_screen()

            case 6:
                c.eliminarLibro()
                u.pasuar()
                u.clear_screen()

            case 7:
                print("Gracias por usar Sistema de Gestión de Biblioteca")
                u.pasuar()
                isActive=False

            case _:
                print("opcion invalida")
    
    except ValueError: 
        print("erro")
