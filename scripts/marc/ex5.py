import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from pandas import DataFrame
from fn import read_data
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns

def plot_distribution_by_gender_age(file_name: str) -> Figure:
    """Generates de N distribution for age and gender in kernel density mode

    Args:
        file_name (str): name of the data file

    Returns:
        Figure: Matplotlib figure
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)
    selected_data: DataFrame = data[["age","sex"]]

    dist_plot: Figure = sns.displot(selected_data, 
                x="age", 
                hue="sex", 
                kind="kde", 
                fill=True)

    return dist_plot

