from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        tick = 1
        reg = 1
        sig_sum = 0
        for instruction in self.input:
            ins_list = instruction.split()
            for ins in ins_list:
                if tick % 40 == 20 :
                    sig_sum += tick*reg
                    # print(f"{tick}*{reg} = {tick*reg}")

                if not (ins == "noop" or ins == "addx"):
                    reg += int(ins)

                tick += 1
        return sig_sum
        
    def calcP2(self):
        tick = 1
        spite_x = 1
        crt_row = ""
        for instruction in self.input:
            ins_list = instruction.split()
            for ins in ins_list:

                spite = [x for x in range(spite_x-1, spite_x+2)]

                if len(crt_row) in spite:
                    crt_row += "#"
                else:
                    crt_row += "."

                if tick % 40 == 0 :
                    print(crt_row)
                    crt_row = ""
                    tick = 0
                
                if not (ins == "noop" or ins == "addx"):
                    spite_x += int(ins)

                tick += 1
