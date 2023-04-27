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

def corrdot(*args, **kwargs) -> Figure:
    """Computes the correlations between numerical values

    Returns:
        Figure: the ax to add to Matplotlib figure
    """
    corr_r = args[0].corr(args[1], 'pearson')
    corr_text = f"{corr_r:2.2f}".replace("0.", ".")
    ax = plt.gca()
    ax.set_axis_off()
    marker_size = abs(corr_r) * 10000
    ax.scatter([.5], [.5], marker_size, [corr_r], alpha=0.6, cmap="coolwarm",
               vmin=-1, vmax=1, transform=ax.transAxes)
    font_size = abs(corr_r) * 40 + 5
    ax.annotate(corr_text, [.5, .5,],  xycoords="axes fraction",
                ha='center', va='center', fontsize=font_size)

def plot_correlation_matrix(file_name: str) -> Figure:
    """Generates the correlation compund matrix plot

    Args:
        file_name (str): name of the data file

    Returns:
        g (Figure): Matplotlib figure
    """

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)
    numerical_data: DataFrame = data.select_dtypes(["number"])

    sns.set(style='white', font_scale=1.6)
    g = sns.PairGrid(numerical_data, aspect=1.4, diag_sharey=False)
    g.map_lower(sns.regplot, lowess=True, ci=False, line_kws={'color': 'black'})
    g.map_diag(sns.distplot, kde_kws={'color': 'black'})
    g.map_upper(corrdot)

    return g


if __name__ == "__main__":
    plot_correlation_matrix("heart_clean.csv")
    plt.show()


