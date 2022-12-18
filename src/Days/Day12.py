from Days.Base.BaseDay import BaseDay
import queue


class Node():

    def __init__(self, x, y, h) -> None:
        self.x = x
        self.y = y
        self.h = ord(h)
        
        self.dist = 999999
        self.par = None
        
        self.is_visited = False
        # self.dist = abs(self.x - dest_pos.x) + abs(self.y - dest_pos.y)

    def get_coords(self):
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"({self.x}/{self.y})-h:{chr(self.h)}-p:({self.par.x if not self.par is None else str()}/{self.par.y if not self.par is None else str()})"
    
    def __add__(self, __o):
        if not type(__o) == type(self):
            raise BaseException("illegal Arument in ADD function")
        else:
            new_x = self.x + __o.x
            new_y = self.y + __o.y
            return (new_x, new_y)

    def __eq__(self, __o: object) -> bool:
        if not type(__o) == type(self):
            return False
        else:
            return self.get_coords() == __o.get_coords()
    
    def __ne__(self, __o: object) -> bool:
        if not type(__o) == type(self):
            return False
        else:
            return not self.get_coords() == __o.get_coords()

    def __lt__(self, __o:object) -> bool:
        if not type(__o) == type(self):
            raise BaseException("illegal Arument in lower then function")
        else:
            return self.get_coords() < __o.get_coords()
    
    def __le__(self, __o:object) -> bool:
        if not type(__o) == type(self):
            raise BaseException("illegal Arument in greater then function")
        else:
            return self.get_coords() <= __o.get_coords()

    def __gt__(self, __o:object) -> bool:
        if not type(__o) == type(self):
            raise BaseException("illegal Arument in greater then function")
        else:
            return self.get_coords() > __o.get_coords()
    
    def __ge__(self, __o:object) -> bool:
        if not type(__o) == type(self):
            raise BaseException("illegal Arument in greater then function")
        else:
            return self.get_coords() >= __o.get_coords()

class Challenge(BaseDay):
    def __init__(self, day=0, is_using_testset=False):
        super().__init__(day, is_using_testset)
        self.is_reverse = False
        # self.vert = [Position(x,y,self.input[y][x]) for y in len(self.input) for x in len(self.input[y])]

    def write_to_file(self, path=None):

        if path is None:
            result_map = []
            for line in self.graph:
                str_line = ""
                for pos in line:
                    str_line += str(chr(pos.h)).upper() if pos.is_visited else str(chr(pos.h))
                result_map.append(str_line)
        else:
            result_map = []
            for line in self.graph:
                str_line = ""
                for pos in line:
                    if pos.is_visited:
                        if pos in path:
                            str_line += "✅"
                        else:
                            str_line += "❌"
                    else:
                        str_line += "❌"
                result_map.append(str_line)

        with open("result_map.txt", "w", encoding="utf-16") as f:
            for l in result_map:
                f.write(l+"\n")                


    def init_graph(self):
        self.graph = []
        
        for y in range(len(self.input)):
            tmp = []
            l = self.input[y]
            for x in range(len(l)):
                pos = Node(x,y,l[x])
                tmp.append(pos)
            self.graph.append(tmp)

    def find_pos(self, marker, new_val=None):
        if new_val is None:
            marker = ord(new_val)

        marker = ord(marker)
        
        for y in range(len(self.graph)):
            l = self.graph[y]
            for x in range(len(l)):
                if l[x].h == marker:
                    l[x].h = ord(new_val)
                    return l[x]
    
    def get_pos(self,pos):
        return self.graph[pos[1]][pos[0]]

    def is_val_move(self, curr_pos, new_coord):
        if new_coord[1] < len(self.graph) and new_coord[0] < len(self.graph[new_coord[1]])\
                and new_coord[1] >= 0 and new_coord[0] >= 0:
            new_pos = self.get_pos(new_coord)
            if new_pos.is_visited:
                return False
            if not self.is_reverse:
                if new_pos.h <= curr_pos.h + 1:
                    return True
            else:
                if new_pos.h + 1 == curr_pos.h or new_pos.h == curr_pos.h or new_pos.h - 1 == curr_pos.h:
                    return True
                # if new_pos.h == curr_pos.h + 1 or new_pos.h == curr_pos.h or new_pos.h == curr_pos.h-1:
                #     return True
        return False

    def get_next_moves(self, c_pos):
        LEFT = (-1, 0)
        DOWN = (0, 1)
        RIGHT = (1, 0)
        UP = (0, -1)
        directions = [UP, RIGHT, DOWN, LEFT]

        moves = []
        for dir in directions:
            pot_new_coord = (c_pos.x + dir[0], c_pos.y + dir[1])
            if self.is_val_move(c_pos, pot_new_coord):
                moves.append(self.get_pos(pot_new_coord))

        return moves

    def BFS(self, start_pos, is_end_condition):
        start_pos.dist = 0
        start_pos.par = None
        start_pos.is_visited = True
        start_pos.dist = 0
        q = []
        q.append(start_pos)
        
        while len(q) > 0:
            if len(q) == 0:
                pass
            curr_p = q.pop(0)
            new_moves = self.get_next_moves(curr_p)
            for move in new_moves:
                move.is_visited = True
                move.dist = curr_p.dist + 1
                move.par = curr_p

                if is_end_condition(move):
                    return move
                if move.get_coords == (142,29):
                    pass

                q.append(move)
        return curr_p

    def calcP1(self):
        self.init_graph()
        start_pos = self.find_pos("S", new_val="a")
        end_pos = self.find_pos("E", new_val="z")

        self.BFS(start_pos, lambda c: c == end_pos)
        path = []
        parent = end_pos.par
        while not parent == None:
            path.insert(0, parent)
            parent = parent.par
        
        self.write_to_file(path)
        

        return len(path)
        
    def calcP2(self):
        end_pos = (145, 20)
        start_pos = (0, 20)

        self.input[end_pos[1]] = self.input[end_pos[1]][:end_pos[0]] + "z" + self.input[end_pos[1]][end_pos[0]+1:]
        self.input[start_pos[1]] = self.input[start_pos[1]][:start_pos[0]] + "a" + self.input[start_pos[1]][start_pos[0]+1:]
        #end_pos = self.find_pos("E", new_val="z")
        #S_pos = self.find_pos("S", new_val="a")
        
        results = []
        for y in range(len(self.input)):
            line = self.input[y]
            for x in range(len(self.input[y])):
                if line[x] == "a":
                    self.init_graph()
                    n_res = self.BFS(self.get_pos((x,y)), lambda c: c.get_coords() == end_pos)
                    if n_res.get_coords() == end_pos:
                        results.append(n_res)

        
        results.sort(key=lambda elem: elem.dist)

        res_node = results.pop(0)
        
        
        
        # ANSATZ ____ starte bei ende und suche solange bis a gefunden wird. _______

        # WARUUUUUMMMMM ???? GEHGT NIOCHTPAHKJSDOIUAGDFZB
        # self.is_reverse = True
        # self.init_graph()
        # end_pos = self.find_pos("E", new_val="z")
        # self.find_pos("S", new_val="a")

        # res_node = self.BFS(end_pos, lambda c: False)
        # # res_node = self.BFS(end_pos, lambda c: c.h == ord("a"))
        
        # self.write_to_file()
        
        # path = []
        # parent = first_node.par
        # while not parent == None:
        #     path.insert(0, parent)
        #     parent = parent.par
        
        print(chr(res_node.h))
        return res_node.dist