import random as rnd
import sys

class Food():
    def __init__(self, name) -> None:
        self.name = name
        self.elo = 1200

    def __str__(self) -> str:
        return f"{self.name}({self.elo:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other) -> bool:
        return self.elo < other.elo

COMMANDS = [
    "q",
    "s",
    "a",
    "d",
    "r",
    "h"
]
INSTRUCTIONS = [
    "Q to Quit.",
    "S for Draw.",
    "A, D for your selection.",
    "R to show the Matchup.",
    "H to show this Message."
]
FOODLIST = [
    "Pizza",
    "Burger",
    "Sushi",
    "Nudles",
    "Lasagne",
    "Chilli",
    "Indian",
    "French Fries",
    "Ice Cream",
    "Kebab",
    "Curry",
    "Pasta"
]

def get_input(prmt):
    res = input(prmt).lower()

    if len(res) > 1:
        res = res[:1]

    if len(res) == 0 or not res in COMMANDS:
        print_instructions(True)
        return get_input("")
    
    # sys.stdout.flush()
    sys.stdin.flush()
    return res
    
def print_instructions(with_wrong_input=False):
    if with_wrong_input: print("Please type a valid input.")
    for l in INSTRUCTIONS:
        res_line = ""
        if with_wrong_input:
            res_line+= "\t-"
        res_line += l
        print(res_line)
    sys.stdout.flush()

def update_score(a, b, is_draw=False):
    s_a = a.elo
    s_b = b.elo

    K = 20

    expec_s_a = 1 / (1 + 10**((s_b-s_a)/400))
    expec_s_b = 1 / (1 + 10**((s_a-s_b)/400))

    if is_draw:
        new_s_a = s_a + K * (0.5 - expec_s_a)
        new_s_b = s_a + K * (0.5 - expec_s_b)
    else:
        new_s_a = s_a + K * (1 - expec_s_a)
        new_s_b = s_b + K * (0 - expec_s_b)

    if new_s_a < 200:
        new_s_a = 200

    if new_s_b < 200:
        new_s_b = 200
    
    a.elo = new_s_a
    b.elo = new_s_b

def print_head(lst,max_count=5):
    lst.sort(reverse=True)
    for i in range(max_count):
        print(f"{i+1}. {lst[i]}")
    sys.stdout.flush()

if __name__ == "__main__":
    foods = []
    for food in FOODLIST:
        foods.append(Food(food))
    
    print_instructions()
    stop = False
    reprint = False
    round_cnt = 0
    is_matchup_round = False

    while not(stop) and round_cnt < (len(FOODLIST)*2):
        if not reprint:
            c = rnd.choices(foods,k=2)
            while c[0] == c[1]:
                c = rnd.choices(foods,k=2)
            matchup = f"{c[0].name}[a] vs. {c[1].name}[d]"

        reprint = False
        
        # print(f'{matchup}')
        inp = get_input(f'{matchup}: ')

        if inp == "q" :
            stop = True
        elif inp == "s":
            update_score(c[1], c[0], is_draw=True)
            is_matchup_round = True
        elif inp == "a":
            update_score(c[0], c[1])
            is_matchup_round = True
        elif inp == "d":
            update_score(c[1], c[0])
            is_matchup_round = True
        elif inp == "r":
            reprint = True
        elif inp == "h":
            print_instructions()
            reprint = True

        if is_matchup_round:
            round_cnt += 1
        
    print("----------------------------------------------")
    print_head(foods)
    print("----------------------------------------------")