# ex2 scatter - Heart disease based on sex and max heart rate
# import
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__))) 

from pandas import DataFrame
from pathlib import Path
from fn import read_data 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# This function uses the columns "thalach", "sex" and "target" from 
# the heart disease dataset passed by parameter to draw 
# a categorical scatterplot. 

def get_condicion_by_hr_sex(file_name: str) -> DataFrame:

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    heart_disease_df: DataFrame = read_data(f_path)

    sns.set_theme(style="whitegrid", palette="muted")

    ax = sns.swarmplot(data=heart_disease_df, x="thalach", y="sex", s=3, hue="target")
    ax.set(ylabel="")
    


if __name__ == "__main__":
    pass
    get_condicion_by_hr_sex("heart_labels.csv")
