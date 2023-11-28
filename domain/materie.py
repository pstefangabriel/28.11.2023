class Materie:
    def __init__(self,id_materie,nume):
        self.__id_materie = id_materie
        self.__nume = nume


    def get_id(self):
        return self.__id_materie


    def get_nume(self):
        return self.__nume