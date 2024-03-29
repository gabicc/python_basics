
class Sport:
    def __init__(self, time, effort):
        self._time = time
        self._effort = effort

    def get_time(self):
        return self._time

    def get_effort(self):
        return self._effort

    def set_time(self, time):
        self._time = time

class Volei(Sport):
    def __init__(self, time, effort, arrangement):
        """ Time = int
         Effort = float
        Arrangement = list"""
        self._time = time
        self._effort = effort
        self._arrangement = arrangement

    def rotate(self):
        prim_elem = self._arrangement[0]
        self._arrangement.remove(prim_elem)
        self._arrangement.append(prim_elem)


    def show_arrangement(self):
        for i in self._arrangement:
            print(i)

class Tenis_de_masa(Sport):
    def __init__(self, time, effort, sets):
        self._time = time
        self._effort = effort
        self._sets = sets

    def get_max_sets(self):
        return self._sets * 2 - 1

