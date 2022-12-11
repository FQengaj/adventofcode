from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calcP1(self):
        window_size = 4
        
        for last_index in range(window_size, len(self.input[0])):
            alphabet = {}
            window = self.input[0][last_index-window_size : last_index]
            for x in range(ord("a"), ord("z")+1):
                alphabet[chr(x)] = list(window).count(chr(x))
            
            if all([c<2 for c in alphabet.values()]):
                return last_index

    def calcP2(self):
        window_size = 14
        
        for last_index in range(window_size, len(self.input[0])):
            alphabet = {}
            window = self.input[0][last_index-window_size : last_index]
            for x in range(ord("a"), ord("z")+1):
                alphabet[chr(x)] = list(window).count(chr(x))
            
            if all([c<2 for c in alphabet.values()]):
                return last_index