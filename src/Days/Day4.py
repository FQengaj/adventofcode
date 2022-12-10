from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        cntr = 0
        snd_cntr = 0
        for pair in self.input:
            e_pair = pair.split(',')
            e1 = e_pair[0].split('-')
            e2 = e_pair[1].split('-')

            rslt = False
            if int(e1[0]) <= int(e2[0]) and int(e1[1]) >= int(e2[1]):
                cntr += 1
                rslt = True
            elif int(e2[0]) <= int(e1[0]) and int(e2[1]) >= int(e1[1]):
                cntr += 1
                rslt = True
            if snd_cntr < 100:
                snd_cntr += 1
                # print(str(snd_cntr) +": "+ str(rslt) +"\t\t"+e1[0]+ ":" +e2[0]+"\t\t"+e1[1]+ ":" + e2[1])
        return cntr

    def calcP2(self):
        cntr = 0
        snd_cntr = 0
        for pair in self.input:
            e_pair = pair.split(',')
            e1 = e_pair[0].split('-')
            e2 = e_pair[1].split('-')

            if int(e1[0]) >= int(e2[0]) and int(e1[0]) <= int(e2[1]):
                cntr += 1
            elif int(e2[0]) >= int(e1[0]) and int(e2[0]) <= int(e1[1]):
                cntr += 1
        return cntr