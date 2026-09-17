import csv
import json


def jsn_loader(csv_path: list, json_path: str) -> list[dict]:
    dict_like: dict[str, list[str]] = {}
    loaded_dicts: list[dict] = []
    for i in csv_path:
        with open(i, "r", encoding='utf-8') as file:
            m: str = ""
            qw = []
            csv_reader = csv.DictReader(file)
            for a in csv_reader:
                b = list(a.keys())
                ar = list(a.values())
                m = b[0]
                qw = b[1]
                dict_like[b[0]] = []
                dict_like[b[0]].append(b[1])
                dict_like[ar[0]] = []
                dict_like[ar[0]].append(ar[1])
                break
            for row in csv_reader:
                key = row.get(f'{m}') or list(row.values())[0]
                value = row.get(f'{qw}') or list(row.values())[1]
                dict_like[key] = []
                dict_like[key].append(value)
        loaded_dicts.append(dict_like)
    if not json_path == "":
        with open(json_path, "w", encoding='utf-8') as js_file:
            json.dump(dict_like, js_file, ensure_ascii=False, indent=5)
    print("All processes done properly")
    return loaded_dicts
