from .csv_converter import jsn_loader
from .argp import get_def_csv, data_josn_pathfinder
from .radomaizer import randomizer
import src.erros


def main():
    filename = input(
        "Write file name for json or type 'skip' for skiping: ").strip()
    if filename == "skip":
        pass
    else:
        if not filename.endswith(".json"):
            filename += ".json"
    jsn = jsn_loader(get_def_csv(), data_josn_pathfinder(filename))
    num = input("Write number of words: ")
    try:
        randomizer(jsn, int(num))
    except src.erros.Less_num:
        print("your choosen number is less then len of csv file")


if __name__ == "__main__":
    main()
