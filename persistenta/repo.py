from exceptii.exceptii import RepoError


class Repo:
    def __init__(self):
        self._entities ={}

    def adauga(self,entitate):
        if entitate.get_id() in self._entities:
            raise RepoError("entitate existenta!")
        self._entities[entitate.get_id()]=entitate

    def sterge_dupa_id(self,id_entitate):
        if id_entitate not in self._entities:
            raise RepoError("entitate inexistenta!")
        del self._entities[id_entitate]

    def modifica(self,entitate):
        if entitate.get_id() not in self._entities:
            raise RepoError("entitate inexistenta!")
        self._entities[entitate.get_id()] = entitate

    def cauta_dupa_id(self,id_entitate):
        if id_entitate not in self._entities:
            raise RepoError("entitate inexistenta!")
        return self._entities[id_entitate]

    def __len__(self):
        return len(self._entities)

    def get_all(self):
        return [self._entities[x] for x in self._entities]

    def isEmpty(self):
        return len(self._entities)==0