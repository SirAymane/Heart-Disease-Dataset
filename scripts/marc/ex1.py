import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from pandas import DataFrame
from pathlib import Path
from fn import read_data

def n_rows(file_name: str) -> int:
    """Count number of rows in datase

    Args:
        file_name (str): name of the data file

    Returns:
        rows (int): number of rows in dataset
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    file: DataFrame = read_data(f_path)

    rows: int = len(file)

    return rows

def count_na_by_col(file_name: str) -> DataFrame:
    """Count NA values for every column

    Args:
        file_name (str): name of the data file

    Returns:
        na_count (DataFrame): DataFrame with the count of NA values by column in original dataset
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name

    print("# Reading file...")
    data: DataFrame = read_data(f_path)

    cols: list[str] = list(data.columns)

    na_count: DataFrame = DataFrame(
        columns=cols
    )

    print("# Counting NaN values by col..")
    for col in cols:
        
        na_count_temp: int = data[col].isna().sum()
        na_count[col] = [na_count_temp]

        print(f"# ...{col}: {na_count_temp} NaN values")

    print("-"*20)

    return na_count


if __name__ == "__main__":
    pass
    # print(count_na_by_col("heart.csv"))
