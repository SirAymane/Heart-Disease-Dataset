# ex3 violin plot - Relationship between levels of exercise induced ST segment depression and exercise induced angina in healthy and sick individuals.
# import
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__))) 

from pandas import DataFrame
from pathlib import Path
from fn import read_data 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# This function uses the columns "exang", "oldpeak" and "target" from 
# the heart disease dataset passed by parameter to draw 
# a cviolinplot. 
def get_condition_exang_oldpeak(file_name: str) -> DataFrame:


    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    heart_disease_df: DataFrame = read_data(f_path)


    plt.figure(figsize=(10,7))
    sns.violinplot(data=heart_disease_df,x='exang',y='oldpeak',hue='target') 


if __name__ == "__main__":
    pass
    get_condition_exang_oldpeak("heart_labels.csv")