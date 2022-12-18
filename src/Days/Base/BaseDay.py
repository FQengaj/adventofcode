class BaseDay():
    solution = 0

    day = 0
    daystr = "day0"

    input = []

    def __init__(self, day=0, is_using_testset=False):
        print(f"init: day{day} - https://adventofcode.com/2022/day/{day}")
        if day == 0:
            raise ValueError()
        self.day = day
        self.daystr = "day" + str(self.day)
        if is_using_testset:
            path =f"../data/day{self.day}_tst.txt"
        else:
            path = f"../data/day{self.day}.txt"
        try:
            with open(path) as file:
                for l in file:
                    # "leere" Zeilen sind nötig bei zu behalten
                    if len(l) > 1:
                        self.input.append(l[:-1])
                    else:
                        self.input.append(l)
        except:
            print(f"___________Input File missing!___________\nDownload current day Input here: https://adventofcode.com/2022/day/{self.day}/input\n__________________________________________________________________")

    def print_p1_solution(self):
        print(f"solution for {self.daystr} p1 = {self.calcP1()}")
    
    def print_p2_solution(self):
        print(f"solution for {self.daystr} p2 = {self.calcP2()}")