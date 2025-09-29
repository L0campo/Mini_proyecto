import modules.mesage as m
import modules.Crud as c
import modules.utli as u

isActive= True

while isActive:
    m.menu()
    try: 
        opcion=int(input("digite una opcion del 1-7: "))
        u.clear_screen()
        match opcion:

            case 1:
                
                print("registro de estudiantes".center(50))
                c.registrar_estudiante (  )
                u.pasuar()
                u.clear_screen()

            case 2:
                print("Agregar materias disponibles".center(50))
                c.agregar_materias()
                u.pasuar()
                u.clear_screen()

            case 3:
                print("Inscribir estudiante a materia".center(50))
                c.inscribir_estudiante()
                u.pasuar()
                u.clear_screen()

            case 4:
                print("Registrar calificación".center(50))
                c.registrar_calificacion()
                u.pasuar()
                u.clear_screen()

            case 5:
                print("ver materias comunes".center(50))
                c.ver_materias_comunes()
                u.pasuar()
                u.clear_screen()

            case 6:
                print("Generar reporte".center(50))
                c.generar_reporte()
                u.pasuar()
                u.clear_screen()

            case 7:
                
                print("Gracias por usar nuestro sistema")
                u.pasuar()
                isActive=False

            case _:
                print("opcion invalida")
    
    except ValueError: 
        print("erro")
