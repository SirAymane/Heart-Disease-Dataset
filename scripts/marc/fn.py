from pandas import DataFrame, read_csv
from pathlib import Path

def read_data(data_path: Path, delimiter: str = ",", decimal: str = ".") -> DataFrame:
    """Reds text file data

    Args:
        data_path (Path): path object to file
        delimiter (str, optional): separator. Defaults to ",".
        decimal (str, optional): decimal. Defaults to ".".

    Returns:
        data (DataFrame): text file parsed to DataFrame
    """

    data: DataFrame = read_csv(data_path, delimiter=delimiter,decimal=decimal, engine="c")

    return data