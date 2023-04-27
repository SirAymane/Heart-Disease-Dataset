import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from fn import read_data
from pandas import DataFrame, melt
from matplotlib.figure import Figure
from matplotlib.pylab import subplots, show
import seaborn as sns
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")

def get_outliers_count(file_name: str) -> DataFrame:
    """Count outlier values for every column.
       Outliers are defined by boxplot default formula

    Args:
        file_name (str): name of the data file

    Returns:
        outlier_count (DataFrame): count of outlier values for every column of the original dataset
    """
    
    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)
    numerical_data: DataFrame = data.select_dtypes(["number"])

    col_list: list[str] = list(numerical_data.columns)

    outlier_count: DataFrame = DataFrame(
        columns=col_list
    )

    for col in col_list:
        q1: float = data[col].quantile(0.25)
        q3: float = data[col].quantile(0.75)
        iqr: float = q3 - q1

        lower_limit: float = q1 - 1.5*iqr
        upper_limit: float = q3 + 1.5*iqr

        outliers: DataFrame = data.query(f"{col} > {upper_limit} or {col}<{lower_limit}")
        n_outliers: DataFrame = len(outliers)

        outlier_count[col] = [n_outliers]

    print(outlier_count)


def facet_boxplots(file_name: str) -> Figure:
    """Generates a boxplot for every numerical column in
       order to visualize the outlier values

    Args:
        file_name (str): name of the data file

    Returns:
        facet_boxplots (Figure): the Matplotlib figure 
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)

    numerical_data: DataFrame = data.select_dtypes(["number"])
    melted_data: DataFrame = melt(numerical_data,value_name="value",var_name="variable")

    facet_boxplots: Figure = sns.catplot(data=melted_data,
                                            x="variable",
                                            y="value",
                                            sharex=False,
                                            sharey=False,
                                            kind="box",
                                            col="variable",
                                            col_wrap=2)

    facet_boxplots.set(xlabel=None,xticklabels=[])
    facet_boxplots.tick_params(bottom=False)

    return facet_boxplots
    

if __name__ == "__main__":
    pass
    # get_outliers_count("heart_labels.csv")
    # facet_boxplots("heart_labels.csv")
    # show()