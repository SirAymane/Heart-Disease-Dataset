# ex1 jointplot - Trend among cholesterol level and resting blood presure
# import
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__))) 

from pandas import DataFrame
from pathlib import Path
from fn import read_data 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# This function uses the columns "chol" i "trestbps" from 
# the heart disease dataset passed by parameter to draw 
# a jointplot. 

def get_relation_chol_trestbps(file_name: str) -> DataFrame:
    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    heart_disease_df: DataFrame = read_data(f_path)
    
    sns.jointplot(data=heart_disease_df,
              x='chol',
              y='trestbps',
              kind='kde',
              cmap='PuBu'
              )

if __name__ == "__main__":
    pass
    get_relation_chol_trestbps("heart_labels.csv")