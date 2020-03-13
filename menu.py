# -*- coding: utf8 -*-
import sys
import platform
from servicio_mensaje import ShortMessageService


class Menu:
    """
    Crea el menu principal para el usuario
    """

    def __init__(self):
        self.service_message = ShortMessageService()
        self.options = { "1": self.add_new_arrival,
                         #"2": self.message_count,
                         #"3": self.get_message,
                         #"4": self.delete_menssage,
                         #"5": self.clear,
                         "6": self.exit
                        }
        

    def display_menu(self):
        """Despliega el menu principal"""
        print("""
               Menu principal
               1. Agregar un mensaje
               2. Mostrar todos los mensajes
               3. Mostrar mensajes no leidos
               4. Buscar un mensaje
               5. Borrar un mensaje
               6. Borrar todos los mensajes
               7. Salir
              """)


    def run(self):
        """ Metodo de entrar para la aplicacion"""
        while True:
            self.display_menu()
            choise = input("ingrese una opcion: ")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("{0} No es una opccion valida!".format(choise))


    def add_new_arrival(self):
        from_number = input("Ingrese el numero: ")
        text_of_sms = input("Agreger el mensaje: ")
        has_been_view="Noleido"
        #self.service_message.add_new_arrival(from_number, text_of_sms, has_been_view)
        print("Mensaje agregado")

    
    def exit(self):
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()