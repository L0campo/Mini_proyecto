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
                c.registrar_estudiante()
                u.pasuar()
                u.clear_screen()

            case 2:
                
                c.agregar_materia()
                u.pasuar()
                u.clear_screen()

            case 3:
                
                c
                u.pasuar()
                u.clear_screen()

            case 4:
                
                c
                u.pasuar()
                u.clear_screen()

            case 5:
                
                c
                u.pasuar()
                u.clear_screen()

            case 6:
                c
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
