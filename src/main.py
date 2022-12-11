from datetime import date
from importlib import import_module

today = date.today().day


today = 7
CurrMod = import_module(f"Days.Day{today}")


if __name__ == "__main__":
    my_p = CurrMod.Challenge(today)
    my_p.print_p1_solution()
    my_p.print_p2_solution()
    