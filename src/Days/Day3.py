from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        l_prio_offset = ord("a") - 1 # 97
        u_prio_offset = ord("A") - 27 # 65

        # print("a = "+ str(ord("a"))) # 97
        # print("z = "+ str(ord("z"))) # 122

        # print("A = " + str(ord("A"))) # 65
        # print("Z = " + str(ord("Z"))) # 90

       
        # bp_index = 1
        t_prio = 0
        for bp in self.input:
            curr_exclude = []
            m_i = len(bp) // 2 
            comp_1 = bp[:m_i]
            comp_2 = bp[m_i:]

            i = 0
            for item in comp_1:
                
                if item in comp_2 and not item in curr_exclude:
                    i = ord(item)
                    if i > ord("A") and i<= ord("Z"):
                        t_prio += i - u_prio_offset
                    elif i > ord("a") and i <= ord("z"):
                        t_prio += i - l_prio_offset
                    
                    curr_exclude.append(item)
        return t_prio

    def calcP2(self):
        l_prio_offset = ord("a") - 1 # 97
        u_prio_offset = ord("A") - 27 # 65

        # print("a = "+ str(ord("a"))) # 97
        # print("z = "+ str(ord("z"))) # 122

        # print("A = " + str(ord("A"))) # 65
        # print("Z = " + str(ord("Z"))) # 90

        
        # bp_index = 1
        t_cost = 0
        rucksack = []
        
        for bp in self.input:
            rucksack.append(bp)

        for i in range(0,len(rucksack),3):
            ex_lst = []
            fst = rucksack[i]
            snd = rucksack[i+1]
            trd = rucksack[i+2]

            for fst_item in fst:
                if fst_item in snd and fst_item in trd and not fst_item in ex_lst:
                    # print(fst_item)
                    i = ord(fst_item)
                    if i > ord("A") and i<= ord("Z"):
                        t_cost += i - u_prio_offset
                    elif i > ord("a") and i <= ord("z"):
                        t_cost += i - l_prio_offset
                    ex_lst.append(fst_item)
        return t_cost