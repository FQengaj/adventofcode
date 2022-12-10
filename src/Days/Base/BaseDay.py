class BaseDay():
    solution = 0

    day = 0
    daystr = "day0"

    input = []

    def __init__(self, day=0):
        print(f"init: day{day}")
        if day == 0:
            raise ValueError()
        self.day = day
        self.daystr = "day" + str(self.day)
        path = f"../data/day{self.day}.txt"
        with open(path) as file:
            for l in file:
                # "leere" Zeilen sind nötig bei zu behalten
                if len(l) > 1:
                    self.input.append(l[:-1])
                else:
                    self.input.append(l)

    def print_p1_solution(self):
        print(f"solution for {self.daystr} p1 = {self.calcP1()}")
    
    def print_p2_solution(self):
        print(f"solution for {self.daystr} p2 = {self.calcP2()}")