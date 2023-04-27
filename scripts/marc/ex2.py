from pandas import DataFrame
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from pathlib import Path
from fn import read_data

def rename_categorical_vars(file_name: str) -> DataFrame:
    """Rename the categorical values to string-label

    Args:
        file_name (str): name of the data file

    Returns:
        data (DataFrame): same DataFrame with labeled values
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)

    print("# Changing sex variable...")
    sex_dict: dict[int,str] = {
        0: "0 - Mujer",
        1: "1 - Hombre"
    }
    data = data.replace({"sex": sex_dict})

    print("# Changing cp variable...")
    cp_dict: dict[int,str] = {
        0: "0 - Angina típica",
        1: "1 - Angina atípica",
        2: "2 - Dolor torácico no anginoso",
        3: "3 - Asintomático"
    }
    data = data.replace({"cp": cp_dict})

    print("# Changing fbs variable...")
    fbs_dict: dict[int,str] = {
        0: "0 - No",
        1: "1 - Sí"
    }
    data = data.replace({"fbs": fbs_dict})

    print("# Changing restecg variable...")
    restecg_dict: dict[int,str] = {
        0: "0 - Normal",
        1: "1 - anormalidad de onda ST-T",
        2: "2 - hipertrofia ventricular probable o definitiva"
    }
    data = data.replace({"restecg": restecg_dict})

    print("# Changing exang variable...")
    exang_dict: dict[int,str] = {
        0: "0 - No",
        1: "1 - Sí"
    }
    data = data.replace({"exang": exang_dict})

    print("# Changing slope variable...")
    slope_dict: dict[int,str] = {
        0: "0 - Ascendente",
        1: "1 - Estanco",
        2: "2 - Descendente"
    }
    data = data.replace({"slope": slope_dict})

    print("# Changing thal variable...")
    thal_dict: dict[int,str] = {
        1: "1 - Normal",
        2: "2 - Defecto crónico",
        3: "3 - Reversible"
    }
    data = data.replace({"thal": thal_dict})

    print("# Changing target variable...")
    target_dict: dict[int,str] = {
        0: "0 - Sano",
        1: "1 - Enfermo"
    }
    data = data.replace({"target": target_dict})

    return data


if __name__ == "__main__":
    pass