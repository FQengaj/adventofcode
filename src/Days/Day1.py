from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        max_cal = [-1,-1,-1]
        max_elf = [-1,-1,-1]
        
        curr_elf = 1
        curr_cal = 0

        for line in self.input:
            if not line == "\n":
                itm_cal = int(line)
                curr_cal += itm_cal
            else:
                for i in range(3):
                    if curr_cal > max_cal[i]:
                        max_cal.insert(i, curr_cal)
                        max_elf.insert(i, curr_elf)

                        max_cal = max_cal[:-1]
                        max_elf = max_elf[:-1]
                        break

                curr_elf += 1
                curr_cal = 0

        return sum(max_cal)

    def calcP2(self):
        return self.calcP1()