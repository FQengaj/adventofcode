from Days.Base.BaseDay import BaseDay
import math

class Monkey:

    items = []

    t_monk = -1
    f_monk = -1

    test_val = -1

    cnt_inspect = 0

    def inspect(self, rel_fac=3):
        self.items[0] = math.floor(self.inspect_(self)/rel_fac)
        self.cnt_inspect += 1

    def test(self):
        return self.items[0] % self.test_val == 0 

    def __init__(self) -> None:
        # self.items.append(3)
        pass

    def __repr__(self) -> str:
        return str(self.items)

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)

    def get_top_two(self, lst):
        
        most_act = [-1,-1]
        for i in range(len(lst)):
            curr_cnt_insp = lst[i]
            for j in range(len(most_act)):
                if most_act[j] < curr_cnt_insp:
                    most_act.insert(j,curr_cnt_insp)
                    del most_act[-1]
                    break
        return most_act

    def init_monkeys(self):
        monkeys = []

        for line in self.input:
            if line == f"Monkey {len(monkeys)}:":
                monkeys.append(Monkey())
                continue
            curr_monk = monkeys[-1]
            if "Starting items: " in line:
                items = line.split(":")[1].replace(",", "").split()
                monkeys[-1].items = [int(i) for i in items]
                # curr_monk = monkeys[-1]
                # for i in items:
                #     curr_monk.append(int(i))
            elif "Operation: " in line:
                eq = line.split("=")[1].split()
                if eq[2] == "old":
                    if eq[1] == "+":
                        curr_monk.inspect_ = lambda self:self.items[0] + self.items[0]
                    else:
                        curr_monk.inspect_ = lambda self:self.items[0] * self.items[0]
                else:
                    curr_monk.insp_val = int(eq[2])
                    if eq[1] == "+":
                        curr_monk.inspect_ = lambda self:self.items[0] + self.insp_val
                    else:
                        curr_monk.inspect_ = lambda self:self.items[0] * self.insp_val
            elif "Test: " in line:
                test_val = line.split()[-1]
                curr_monk.test_val = int(test_val)
            elif "If true: " in line:
                t_monk = line.split()[-1]
                curr_monk.t_monk = int(t_monk)
            elif "If false: " in line:
                f_monk = line.split()[-1]
                curr_monk.f_monk = int(f_monk)

        return monkeys

    def calcP1(self):
        monkeys = self.init_monkeys()
        
        for i in range(20):
            for monk in monkeys:
                while len(monk.items) >0:
                    monk.inspect()
                    if monk.test():
                        i_next_monk = monk.t_monk
                    else:
                        i_next_monk = monk.f_monk
                    monkeys[i_next_monk].items.append(monk.items.pop(0))
        
        lst = [monk.cnt_inspect for monk in monkeys]
        most_act = self.get_top_two(lst)

        return most_act[0]*most_act[1]

        
    def calcP2(self):
        monkeys = self.init_monkeys()
        for i in range (1, 10001):
            for monk in monkeys:
                while len(monk.items) > 0:
                    monk.inspect(rel_fac=1)
                    if monk.test():
                        i_next_monk = monk.t_monk
                    else:
                        i_next_monk = monk.f_monk
                    curr_item = monk.items.pop(0)
                    # if not curr_item in monkeys[i_next_monk].items:
                    monkeys[i_next_monk].items.append(curr_item)

            if i == 1 or i == 20 or (i%1000)==0:        
                lst = [monk.cnt_inspect for monk in monkeys]
                print(f"Round {i}:\t{lst}")
        
