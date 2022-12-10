from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
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
        self.instructions = self.input[count_lines:]

        self.cargos = {}
        terminals = self.start_map[-1].split()
        for terminal in terminals:
            self.cargos[int(terminal)] = []
        
        for i in range(len(self.start_map)-1):
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
                    self.cargos[x] = cargo[cargo.find("[")+1]
                
                # print(cargo)

            # curr_term = terminals[-1]
            # for x in range(len(curr_line), 0, -4):
                

        print(self.cargos)
        
    def calcP1(self):
        pass
    
    def calcP2(self):
        pass