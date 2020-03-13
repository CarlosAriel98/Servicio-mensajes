#-*-utf-8-*-
import datetime


#variables glovales
id_message = 0


class messages:
    """
    Simula un mensaje enviador por un usuario con un
    programa de mensajeria
    """

    def __init__(self, from_number="", text_of_sms="", has_been_viewed=""):
        """
        Inicia un mensaje con valores de from_number,
        time_arrived, text_of_sms enviadas por el usario(esto
        se separa por comas) y automaticamente inserta la vista
        """
        self.from_number = from_number
        self.text_of_sms = text_of_sms
        self.has_been_viewed = has_been_viewed
        self.create_time = datetime.date.today()
        global id_message
        id_message += 1
        self.id = id_message

        


    
