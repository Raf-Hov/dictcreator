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
