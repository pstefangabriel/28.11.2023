from persistenta.repo import Repo


class FileRepo(Repo):
    def __init__(self,cale_fisier,parse_entity,entity_to_line):
        Repo.__init__(self)
        self.__cale_fisier =cale_fisier
        self.__parse_entity = parse_entity
        self.__entity_to_line = entity_to_line

    def __read_all_from_file(self):
        with open(self.__cale_fisier,"r") as f:
            self._entities.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entity = self.__parse_entity(line)
                    self._entities[entity.get_id()]=entity

    def __write_all_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for entity_id in self._entities:
                f.write(self.__entity_to_line(self._entities[entity_id])+"\n")



    def adauga(self, entitate):
        self.__read_all_from_file()
        Repo.adauga(self,entitate)
        self.__write_all_to_file()

    def sterge_dupa_id(self,id_entitate):
        self.__read_all_from_file()
        Repo.sterge(self, id_entitate)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return Repo.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return Repo.__len__(self)
