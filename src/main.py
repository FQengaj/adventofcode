from datetime import date
from importlib import import_module
import sys

today = date.today().day


today = 13
try:
    CurrMod = import_module(f"Days.Day{today}")
except:
    with open(f"Days/Day{today}.py", "w") as d_file:
        with open(f"../data/template/Challenge_class.txt", "r") as s_file:
            d_file.write(s_file.read())

finally:
    CurrMod = import_module(f"Days.Day{today}")


if __name__ == "__main__":
    part_select = sys.argv[1]
    try:
        use_testset = sys.argv[2] == "test"
    except IndexError:
        use_testset = False
    my_p = CurrMod.Challenge(today, use_testset)

    if part_select == "p1":
        my_p.print_p1_solution()
    elif part_select == "p2":
        my_p.print_p2_solution()
    
