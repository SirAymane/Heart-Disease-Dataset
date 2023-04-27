from pandas import DataFrame, read_csv
from pathlib import Path

def read_data(data_path: Path, delimiter: str = ",", decimal: str = ".") -> DataFrame:

    data: DataFrame = read_csv(data_path, delimiter=delimiter,decimal=decimal, engine="c")

    return data