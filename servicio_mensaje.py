#-*-utf-8-*-

class ShortMessageService:
    """
    Contiene las funciones principales del mensaje(agregar, buscar y eliminar)
    """

    def __init__(self):
        """ Crea una bandeja limpia """
        self.my_box = list()
    
    def add_new_arrival(self, from_number="", text_of_sms=""):
        """ Crea un mensaje y lo agrega a la bandeja de enviados """
    

    def message_count(self):
        """ Muestra la cantidad de mensajes en la bandeja """
        en_Lista = str(len(self.my_box))
    
    
    def get_unread_indexes(self, has_been_viewed = "Noleido"):
        """ Muestra la lista de los mensajes sin leer """
        for msm in self.my_box:
            if str(msm.has_been_viewed) == str(has_been_viewed):
                return msm

    
    def _search_note(self, id_message):
        """
        Busca los mensajes enviados
        Funcion privada
        """

        for sms in self.my_box:
            if str(msm.id) == str(id_message):
                return msm
        
        return None

    def delete_message(self, id_message)
    """ Elimina un mensaje"""
    msm = self._search_note(id_message)

    if sms:
        sefl.my_box.remove(id_message)
        return True
    else:
        print("no existe un mensaje con el id: {0}")
        self.format(id_message)
        return False
    
    def clear(self):
        """ Elimina todos los mensajes"""
    
