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
    
    
    def get_unread_indexes(self):
        """ Muestra la lista de los mensajes sin leer """
        for msm in self:
            if str(m.id) == str(note_id):
                return NotADirectoryError