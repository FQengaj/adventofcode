from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        op_code = {"A":"Rock", "B":"Paper", "C":"Scissors"}
        my_code = {"X":"Rock", "Y":"Paper", "Z":"Scissors"}

        p_pick = {"Rock":1, "Paper":2, "Scissors":3}
        p_outcome = {"Win":6, "Draw":3, "Loose":0}


        
        total_points = 0
        for p in self.input:
            # p = p[:-1]
            op_pick = p[0]
            my_pick = p[-1]
            total_points += p_pick[my_code[my_pick]]
            i_op_pick = list(op_code.keys()).index(op_pick)
            i_my_pick = list(my_code.keys()).index(my_pick)

            outcome = (i_my_pick + 2) % 3
            if outcome == i_op_pick:
                total_points += p_outcome["Win"]
            elif i_op_pick == i_my_pick:
                total_points += p_outcome["Draw"]
            else:
                total_points += p_outcome["Loose"]
        
        return total_points
    
    def calcP2(self):
        op_code = {"A":"Rock", "B":"Paper", "C":"Scissors"}
        ex_outcome = {"X":"Loose", "Y":"Draw", "Z":"Win"}

        p_pick = {"Rock":1, "Paper":2, "Scissors":3}
        p_outcome = {"Win":6, "Draw":3, "Loose":0}


        
        total_points = 0
        for p in self.input:
            # p = p[:-1]
            op_pick = p[0]
            i_op_pick = list(op_code.keys()).index(op_pick)
            outcome = p[-1]

            if outcome == "X":
                mypick = list(p_pick.values())[(i_op_pick + 2) % 3]
            elif outcome == "Y":
                mypick = p_pick[op_code[op_pick]]
            else:
                mypick = list(p_pick.values())[(i_op_pick - 2) % 3]
            
            total_points += p_outcome[ex_outcome[outcome]]
            total_points += mypick

        return total_points