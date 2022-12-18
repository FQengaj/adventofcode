from Days.Base.BaseDay import BaseDay
import math

class Position():
    def __init__(self, x, y, h) -> None:
        self.x = x
        self.y = y
        self.h = ord(h)

    def __repr__(self) -> str:
        return f"({self.x}/{self.y})-h:{self.h}-s:{self.score if hasattr(self, 'score') else str()}"
    
    def __eq__(self, __o: object) -> bool:
        if not type(__o) == type(self):
            return False
        else:
            return (self.x == __o.x and self.y == __o.y) 

    def set_score(self, score):
        self.score = score


class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def discover_next_moves(self, curr_pos):
        next_posible_moves = []
        if curr_pos.y > 0:
            up = Position(curr_pos.x, curr_pos.y-1, self.input[curr_pos.y-1][curr_pos.x])
            if self.is_valid_move(curr_pos, up):
                next_posible_moves.append(up)

        if curr_pos.y < len(self.input)-1:
            down = Position(curr_pos.x, curr_pos.y+1, self.input[curr_pos.y+1][curr_pos.x])
            if self.is_valid_move(curr_pos, down):
                next_posible_moves.append(down)

        if curr_pos.x > 0:
            left = Position(curr_pos.x-1, curr_pos.y, self.input[curr_pos.y][curr_pos.x-1])
            if self.is_valid_move(curr_pos, left):
                next_posible_moves.append(left)

        if curr_pos.x < len(self.input[curr_pos.y])-1:
            right = Position(curr_pos.x+1, curr_pos.y, self.input[curr_pos.y][curr_pos.x+1])
            if self.is_valid_move(curr_pos, right):
                next_posible_moves.append(right)

        return next_posible_moves


    def get_pos(self, marker):
        for y in range(len(self.input)):
            line = self.input[y]
            for x in range (len(line)):
                curr_h = line[x]
                if curr_h == marker:
                    return Position(x,y, curr_h)

    def calc_score(self, curr_pos, end_pos):
        dx = abs(curr_pos.x - end_pos.x)
        dy = abs(curr_pos.y - end_pos.y)

        dh = end_pos.h - curr_pos.h
        
        score = math.sqrt(dx**2 + dy**2)# + dh
        curr_pos.set_score(score)

        return score

    def is_valid_move(self, curr_pos, next_pos):
        return not (next_pos.h - curr_pos.h > 2)
    
    def calcP1(self):
        emoji = "⬆️ ⬇️ ⬅️ ➡️"
        
        curr_pos = self.get_pos("S")
        self.input[curr_pos.y].replace("S", "a")
        curr_pos.h = ord("a")
        dest_pos = self.get_pos("E")
        self.input[dest_pos.y].replace("E", "z")
        dest_pos.h = ord("z")

        depth = 0
        # stack = [curr_pos]
        path = [curr_pos]
        exclusion = []
        while not curr_pos == dest_pos:
            # calc next moves
            next_posible_moves = self.discover_next_moves(curr_pos)
            next_posible_moves.sort(key=lambda elem: self.calc_score(elem, dest_pos))
            # print(f"path: {path}")
            # for pos in next_posible_moves:
            #     print(pos)
            # print("--------------------------------------------------")
            next_best_pos = next_posible_moves.pop(0)
            backtrack = False
            while next_best_pos in path or next_best_pos in exclusion:
                try:
                    next_best_pos = next_posible_moves.pop(0)
                except IndexError:
                    #backtrack and add curr_pos to exclusion
                    exclusion.append(curr_pos)
                    backtrack = True
                    break
            if backtrack:
                del path[-1]
                curr_pos = path[-1]
            else:
                path.append(next_best_pos)
                curr_pos = next_best_pos
            depth +=1
            if depth == 15:
                pass
        lst = [elem for elem in path]
        with open("result_path.csv", "w") as f:
            for x in lst:
                f.write(f"{x.x},{x.y}\n")
        
        for elem in lst:
            self.input[elem.y] = self.input[elem.y][:elem.x] + "X" +  self.input[elem.y][elem.x+1:]
        with open("result_map.txt", "w") as f:
            for i in self.input:
                f.write(i+"\n")
        return len(path) #[f"{elem.x,elem.y}" for elem in path]
        
    def calcP2(self):
        pass