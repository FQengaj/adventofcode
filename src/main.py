from datetime import date
from importlib import import_module

today = date.today().day


today = 11
try:
    CurrMod = import_module(f"Days.Day{today}")
except:
    with open(f"Days/Day{today}.py", "w") as d_file:
        with open(f"../data/template/Challenge_class.txt", "r") as s_file:
            d_file.write(s_file.read())

finally:
    CurrMod = import_module(f"Days.Day{today}")


if __name__ == "__main__":
    my_p = CurrMod.Challenge(today)
    my_p.print_p1_solution()
    my_p.print_p2_solution()
    