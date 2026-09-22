import sys
import src.erros
from .radomaizer import randomizer
from .csv_converter import jsn_loader
from .argp import get_data_files, data_josn_pathfinder


def main():
    lang = input("Choose language (eng / fr): ").strip().lower()
    folder = "data_for_fr" if lang == "fr" else "data"
    try:
        all_files = get_data_files(folder)
    except Exception as e:
        print(e)
        return
    print("\nAvailable files in data folder:")
    for i, file_path in enumerate(all_files, 1):
        print(f"{i} : {file_path.name}")
    sys.stdout.flush()
    file_choice = input("\nWrite the numbers of the files you want to use (e.g., '1 3'): ").strip().replace(",", " ")
    if not file_choice:
        print("Error: No files selected!")
        return
    selected_files = []
    for c in file_choice.split():
        try:
            idx = int(c)
            if 1 <= idx <= len(all_files):
                selected_files.append(all_files[idx - 1])
        except ValueError:
            pass
    if not selected_files:
        print("Error: Invalid files selected!")
        return
    filename = input("\nWrite file name to save as new JSON (or press enter to skip): ").strip()
    if filename and not filename.endswith(".json"):
        filename += ".json"
    jsn = jsn_loader(selected_files, data_josn_pathfinder(filename))
    mix_all = {}
    for d in jsn.values():
        mix_all.update(d)
    jsn["mix_all"] = mix_all
    available_dicts = list(jsn.keys())
    print("\nAvailable dictionaries from loaded files:")
    for i, name in enumerate(available_dicts, 1):
        print(f"{i} : {name}")
    sys.stdout.flush()
    print("\nWrite the numbers of the dictionaries you want to mix.")
    choice_input = input("Your choice: ").strip().replace(",", " ")
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
    num = input("\nWrite number of words: ").strip()
    order_choice = input("Randomize words? (y/n): ").strip().lower()
    is_random = order_choice != 'n'
    sys.stdout.flush()
    try:
        randomizer(jsn, int(num), chosen_name, is_random)
    except src.erros.Less_num:
        print("Your chosen number is greater than the total length of the selected files.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
