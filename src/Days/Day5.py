from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
        
    def parse_input(self):
        # parse input 
        # [D]                     [N] [F]    
        # [H] [F]             [L] [J] [H]    
        # [R] [H]             [F] [V] [G] [H]
        # [Z] [Q]         [Z] [W] [L] [J] [B]
        # [S] [W] [H]     [B] [H] [D] [C] [M]
        # [P] [R] [S] [G] [J] [J] [W] [Z] [V]
        # [W] [B] [V] [F] [G] [T] [T] [T] [P]
        # [Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
        #  1   2   3   4   5   6   7   8   9 
        #
        #move 1 from 3 to 9
        #move 2 from 2 to 1
        count_lines = 0
        for l in self.input:
            count_lines +=1
            if l == "\n":
                break
        self.start_map = self.input[:count_lines-1]
        self.instr = self.input[count_lines:]

        self.cargos = {}
        terminals = self.start_map[-1].split()
        for terminal in terminals:
            self.cargos[int(terminal)] = []
        
        for i in range(len(self.start_map)-1,-1,-1):
            curr_line = self.start_map[i]
            # for each terminal split the line in 3 long substrings.
            # with that remove the intermediate spaces.
            # last character is not space.
            last_end_of_term = 0
            for x in range(1,len(terminals)+1):
                end_of_term = (x*4)-1
                cargo = curr_line[last_end_of_term: end_of_term]
                last_end_of_term = end_of_term
                if "[" in cargo:
                    self.cargos[x].append(cargo[cargo.find("[")+1])
        
        # ---------- Parse instructions ----------
        self.instructions = []
        for i in self.instr:
            curr_inst = i.split()
            self.instructions.append({"move":int(curr_inst[1]), "from":int(curr_inst[3]), "to":int(curr_inst[5])})

    def calcP1(self):
        self.parse_input()
        for instruction in self.instructions:
            # print(instruction)
            move_count = instruction["move"]
            origin = instruction["from"]
            dest = instruction["to"]

            for i in range(move_count):
                self.cargos[dest].append(self.cargos[origin].pop())
        
        resstr = ""
        for c in self.cargos:
            # print(self.cargos[c][-1])
            resstr += self.cargos[c][-1]
        return resstr    

    def calcP2(self):
        self.parse_input()
        for instruction in self.instructions:
            move_count = instruction["move"]
            origin = instruction["from"]
            dest = instruction["to"]
            
            negcntr = move_count*-1
            for i in range(move_count):
                item = self.cargos[origin].pop(negcntr+i)
                self.cargos[dest].append(item)

        resstr = ""
        for c in self.cargos:
            if len(self.cargos[c]) > 0:
                resstr += self.cargos[c][-1]
        return resstr