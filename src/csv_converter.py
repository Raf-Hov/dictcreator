import csv
import json
from pathlib import Path
from .erros import Csv_not_found


def get_def_csv() -> list:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    if not data_dir.exists():
        raise FileNotFoundError
    csv_file = list(data_dir.glob("*.csv"))
    if not csv_file:
        raise Csv_not_found("csv files not found")
    return csv_file


def data_josn_pathfinder(name: str) -> str:
    if name == "":
        return ""
    data_json_dir = Path(__file__).resolve().parent.parent / "data_json"
    data_json_dir.mkdir(parents=True, exist_ok=True)
    full_file_path = data_json_dir / name
    return str(full_file_path)


def jsn_loader(csv_paths: list, json_path: str) -> dict[str, dict]:
    loaded_dicts: dict[str, dict] = {}
    for path in csv_paths:
        dict_like: dict[str, list[str]] = {}
        with open(path, "r", encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 2:
                    key = row[0].strip()
                    values = [v.strip() for v in row[1:] if v.strip()]
                    if key in dict_like:
                        dict_like[key].extend(values)
                    elif values:
                        dict_like[key] = values
        file_name = path.stem 
        loaded_dicts[file_name] = dict_like
    if json_path != "":
        with open(json_path, "w", encoding='utf-8') as js_file:
            json.dump(loaded_dicts, js_file, ensure_ascii=False, indent=5)
    print("All processes done properly")
    return loaded_dicts
