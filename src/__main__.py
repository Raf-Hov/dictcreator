import sys
import src.erros
from .radomaizer import randomizer
from .csv_converter import jsn_loader
from .argp import get_def_csv, data_josn_pathfinder


def main():
    lang = input("Choose language (eng / fr): ").strip().lower()
    folder = "data_for_fr" if lang == "fr" else "data"
    filename = input("Write file name for json or press enter for skipping: ").strip()
    if filename and not filename.endswith(".json"):
        filename += ".json"
    jsn = jsn_loader(get_def_csv(folder), data_josn_pathfinder(filename))
    mix_all = {}
    for d in jsn.values():
        mix_all.update(d)
    jsn["mix_all"] = mix_all
    available_dicts = list(jsn.keys())
    print("\nAvailable dictionaries:")
    for i, name in enumerate(available_dicts, 1):
        print(f"{i} : {name}")
    sys.stdout.flush()
    print("\nWrite the numbers of the dictionaries you want to use.")
    print("Example: '1' for a single dictionary, or '1 3' to combine them.")
    choice_input = input("Your choice: ").strip()
    choice_input = choice_input.replace(",", " ")
    choices = choice_input.split()
    if not choices:
        print("Error: No input provided!")
        return
    chosen_name = "custom_mix"
    custom_dict = {}
    try:
        for c in choices:
            idx = int(c)
            if idx < 1 or idx > len(available_dicts):
                print(f"Error: Invalid number '{idx}'!")
                return
            dict_name = available_dicts[idx - 1]
            custom_dict.update(jsn[dict_name])
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
    jsn[chosen_name] = custom_dict
    num = input("Write number of words: ").strip()
    sys.stdout.flush()
    try:
        randomizer(jsn, int(num), chosen_name)
    except src.erros.Less_num:
        print("Your chosen number is greater than the length of the csv file.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
