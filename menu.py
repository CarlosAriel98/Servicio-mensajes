# -*- coding: utf8 -*-
import sys
import os
import platform
from servicio_mensaje import ShortMessageService


class Menu:
    """
    Crea el menu principal para el usuario
    """

    def __init__(self):
        self.service_message = ShortMessageService()
        self.options = { "1": self.add_new_arrival,
                         "2": self.message_count,
                         "3": self.get_unread_index,
                         "4": self.get_message,
                         "5": self.delete_menssage,
                         "6": self.clear,
                         "7": self.exit
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

    
    def press_enter(self):
        """Realisa una pausar pare pedirle al usuario precionar una tecla"""
        input("\nPrecione Enter para continuar")


    def clear_screen(self):
        """
        verificar la plataforma del sistema operatico
        del usuario y limpia la pantalla dependiendo del SO del usuario
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")

            

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
        self.clear_screen()
        from_number = input("Ingrese el numero: ")
        text_of_sms = input("Agreger el mensaje: ")
        has_been_view="noleido"
        self.service_message.add_new_arrival(from_number, text_of_sms, has_been_view)
        print("Mensaje agregado")
        self.press_enter()


    def message_count(self):
        self.service_message.message_count()
        self.press_enter()

    
    def get_unread_index(self, leido="noleido"):
        self.clear_screen
        """ Busca los mensajes no leidos """
        My_box = self.service_message.my_box
        for box in My_box:
            print("ide: {0}\nNumero: {1}\ntexto: {2}\nFecha: {3} {4}"
             .format(box.id, box.from_nunver, box.text_of_sms, box.create_time, box.has_been_viewed))
        self.press_enter()


    def get_message(self):
        """ Despliega una nota"""
        self.clear_screen()
        leido="ledio"
        idmessage = input("Ingrese el ide del mensaje: ")
        My_box = self.service_message.my_box
        for box in My_box:
            if str(box.id) == str(idmessage):
                print("Id: {0}\nNumero: '{1}'\ntexto: {2}\nFecha: {3} {4}"
                .format(box.id, box.from_number, box.text_of_sms, box.create_time, box.has_been_viewed))
                self.service_message.modify_message(box.id, box.from_number, box.text_of_sms, leido)
        self.press_enter()


    def delete_menssage(self):
        idmessage = input("ingrese el id del mensaje: ")
        self.service_message.delete_message(idmessage)
        self.press_enter()

    
    def clear(self):
        self.service_message.clear()
        self.press_enter()

    
    def exit(self):
        """Cierra la aplicacion"""
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()

