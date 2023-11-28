class Student:
    def __init__(self, id_student, nume, valoare):
        self.__id_student = id_student
        self.__nume = nume
        self.__valoare = valoare

    def get_id(self):
        return self.__id_student

    def get_nume(self):
        return self.__nume


    def get_valoare(self):
        return self.__valoare

