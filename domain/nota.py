class Nota:
    def __init__(self,id_nota,student,materie,valoare_nota):
        self.__id_nota = id_nota
        self.__student = student
        self.__materie = materie
        self.__valoare_nota = valoare_nota

    def get_id(self):
        return self.__id_nota