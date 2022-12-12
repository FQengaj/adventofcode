from Days.Base.BaseDay import BaseDay

class Challenge(BaseDay):
    def __init__(self, day=0):
        super().__init__(day)
    
    def calc_diff(self, head, tail):
        return abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    
    def calc_diff_vec(self, head, tail):
        x = head[0]-tail[0]
        y = head[1]-tail[1]
        return (x,y)
    
    def calc_move_vec(self, head, tail):
        diff_vec = self.calc_diff_vec(head,tail)
        x, y = 0, 0
        if abs(diff_vec[0]) > 1 and abs(diff_vec[1]) > 1:
            if diff_vec[0] > 1:
                x = diff_vec[0]-1
            else:
                x = diff_vec[0]+1

            if diff_vec[1] > 1:
                y = diff_vec[1]-1
            else:
                y = diff_vec[1]+1
        elif abs(diff_vec[0]) > 1:
            if diff_vec[0] > 1:
                x = diff_vec[0]-1
            else:
                x = diff_vec[0]+1
            y = diff_vec[1]
        elif abs(diff_vec[1]) > 1:
            if diff_vec[1] > 1:
                y = diff_vec[1]-1
            else:
                y = diff_vec[1]+1
            x = diff_vec[0]
        return (x,y)

    
    def calcP1(self):
        head = (0,0)
        last_head = (0,0)
        tail = (0,0)
        tail_pos = set()
        for l in self.input:
            instruction = l.split()
            dir = instruction[0]
            for i in range(int(instruction[1])):
                last_head = (head[0], head[1])
                if dir == "L":
                    head = (head[0]-1, head[1])
                elif dir == "R":
                    head = (head[0]+1, head[1])
                elif dir == "U":
                    head = (head[0], head[1]-1)
                elif dir == "D":
                    head = (head[0], head[1]+1)

                diff = self.calc_diff(head, tail)
                if diff > 2:
                    tail = (last_head[0], last_head[1])
                elif diff > 1:
                    if abs(head[0]-tail[0]) > 1:
                        if head[0] > tail[0]:
                            tail = (head[0]-1, tail[1])
                        else:
                            tail = (head[0]+1, tail[1])
                    elif abs(head[1]-tail[1]) > 1:
                        if head[1] > tail[1]:
                            tail = (tail[0], head[1]-1)
                        else:
                            tail = (tail[0], head[1]+1)

                tail_pos.add(tail)
        
        return len(tail_pos)

    def calcP2(self):
        body = [(0,0) for x in range(10)]
        tail_pos = set()
        i_head = 0
        i_tail = len(body)-1

        for l in self.input:
            instruction = l.split()
            dir = instruction[0]
            for i in range(int(instruction[1])):
                head = body[i_head]
                if dir == "L":
                    body[i_head] = (head[0]-1, head[1])
                elif dir == "R":
                    body[i_head] = (head[0]+1, head[1])
                elif dir == "U":
                    body[i_head] = (head[0], head[1]-1)
                elif dir == "D":
                    body[i_head] = (head[0], head[1]+1)
                
                for knot in range (1,len(body)):
                    prev_knot = body[knot-1]
                    curr_knot = body[knot]
                    diff = self.calc_diff(curr_knot, prev_knot)

                    if diff > 2:
                        move_vec = self.calc_move_vec(prev_knot, curr_knot)
                        
                        body[knot] = (curr_knot[0]+move_vec[0], curr_knot[1]+move_vec[1])

                    elif diff > 1:
                        if abs(prev_knot[0]-curr_knot[0]) > 1:
                            if prev_knot[0] > curr_knot[0]:
                                body[knot] = (prev_knot[0]-1, curr_knot[1])
                            else:
                                body[knot] = (prev_knot[0]+1, curr_knot[1])
                        elif abs(prev_knot[1]-curr_knot[1]) > 1:
                            if prev_knot[1] > curr_knot[1]:
                                body[knot] = (curr_knot[0], prev_knot[1]-1)
                            else:
                                body[knot] = (curr_knot[0], prev_knot[1]+1)
                tail_pos.add(body[i_tail])
        return len(tail_pos)