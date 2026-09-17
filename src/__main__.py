from .csv_converter import jsn_loader
from .argp import get_def_csv, data_josn_pathfinder
from .radomaizer import randomizer
import src.erros
import sys


def main():
    filename = input(
        "Write file name for json or press enter for skiping: ")
    if filename == "":
        pass
    else:
        if not filename.endswith(".json"):
            filename += ".json"
    jsn = jsn_loader(get_def_csv(), data_josn_pathfinder(filename))
    k = len(jsn)
    print("Enter the number of section ", end="")
    for i in range(k):
        if i < k - 1:
            print(f"{i}, ", end="")
        else:
            print(f"{i} :", end="")
    sys.stdout.flush()
    n = sys.stdin.readline()
    num = input("Write number of words: ")
    sys.stdout.flush()
    try:
        randomizer(jsn, int(num), int(n))
    except src.erros.Less_num:
        print("your choosen number is less then len of csv file")


if __name__ == "__main__":
    main()
