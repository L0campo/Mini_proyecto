import modules.Crud as c
import modules.messages as m
import modules.utiz as u



isActive= True
while isActive:
    m.menu()
    try: 
        opcion=int(input("digite una opcion del 0-4: "))
        match opcion:

            case 0:

                isActive=False

            case 1:
                u.clear_screen()
                c.add_game()
                input("precione Enter para continuar...")
                u.clear_screen()

            case 2:
                u.clear_screen()
                c.view_games()
                input("precione Enter para continuar...")
                u.clear_screen()

            case 3:
                u.clear_screen()
                c.complete_game()
                input("precione Enter para continuar...")
                u.clear_screen()

            case 4:
                u.clear_screen()
                c.complete_game()
                input("precione Enter para continuar...")
                u.clear_screen()

            case _:
                print("eleccion invalida")













    except ValueError: 
         print("erro")