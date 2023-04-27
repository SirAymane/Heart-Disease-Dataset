import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import warnings
warnings.filterwarnings("ignore")

from sklearn.tree import DecisionTreeClassifier 
from dtreeviz.trees import dtreeviz 
from dtreeviz.trees import DTreeViz

from pandas import DataFrame, crosstab
from fn import read_data
from pathlib import Path
import numpy as np

def binarize(data: DataFrame, col: str = "target") -> DataFrame:
    """Parse labels to 0 and 1 values

    Args:
        data (DataFrame): data to be parsed
        col (str, optional): column to binarize.

    Returns:
        binarized (DataFrame): same DataFrame with binary parsed selected column
    """

    unique_values: list[str] = list(data[col].unique())

    binary_values: list[int] = [0,1]

    binary_dict: dict[str,int] = dict(zip(unique_values,binary_values))

    binarized: DataFrame = data.replace({col: binary_dict})

    return binarized


def get_train_test_datasets(file_name: str, sample_train: float = 0.7) -> tuple[DataFrame,DataFrame]:
    """Split a Dataframe in train and test data according to a percentage of sample size

    Args:
        file_name (str): name of the data file
        sample_train (float, optional): percentage that goes to train data. Defaults to 0.7.

    Returns:
        train, test (tuple[DataFrame,DataFrame]): tuple of Dataframes
    """

    assert sample_train != 1, "All data cannot be choosen for train sample"
    assert sample_train != 0, "Must be some data for the train dataset"

    f_path: Path = Path(__file__).parents[2]/"data"/file_name
    data: DataFrame = read_data(f_path)

    msk = np.random.rand(len(data)) < sample_train

    train: DataFrame = data[msk]
    test: DataFrame = data[~msk]

    return train,test 

def get_tree_decision_model(train: DataFrame, y_col: str = "target") -> DecisionTreeClassifier:
    """Fits a decision tree model

    Args:
        train (DataFrame): data used to train the model
        y_col (str, optional): target column to predict. Defaults to "target".

    Returns:
        clf (DecisionTreeClassifier): trained model
    """

    predictors: DataFrame = train.drop(y_col, axis=1)
    y: DataFrame = train[[y_col]]

    clf: DecisionTreeClassifier = DecisionTreeClassifier(random_state=1234, 
                                                            max_depth=5,
                                                            max_features="auto")
    clf.fit(predictors,y)

    return clf

def get_confusion_matrix(model: DecisionTreeClassifier, 
                        data: DataFrame, 
                        y_col: str = "target",
                        values: str = "absolute") -> DataFrame:
    """Generates a confusion matrix based on observed and predicted values

    Args:
        model (DecisionTreeClassifier): model used to predict
        data (DataFrame): data used to test
        y_col (str, optional): variable to predict. Defaults to "target".
        values (str, optional): output format (absolute, relative). Defaults to "absolute".

    Returns:
        confusion_matrix (DataFrame): the confusion matrix
    """

    train_data_x: DataFrame = data.drop([y_col], axis=1)
    observed_y: list[int] = data[y_col].tolist()

    prediction: list[int] = model.predict(train_data_x)

    cross_data: DataFrame = DataFrame(
        data={
            "observed_target": observed_y,
            "predicted_target": prediction
        }
    )

    confussion_matrix: DataFrame = crosstab(cross_data["observed_target"],
                                            cross_data["predicted_target"],
                                            rownames=["Observado"],
                                            colnames=["Predecido"])

    n_observations: int = confussion_matrix.to_numpy().sum()

    if values == "relative":
        confussion_matrix = confussion_matrix / n_observations

    print(confussion_matrix)

def plot_decision_tree(model: DecisionTreeClassifier, data: DataFrame, y_col: str = "target") -> DTreeViz:
    """Plot decision tree

    Args:
        model (DecisionTreeClassifier): model to predict
        data (DataFrame): data to predict
        y_col (str, optional): variable to predict. Defaults to "target".

    Returns:
        DTreeViz: decision tree
    """

    predictors: DataFrame = data.drop(y_col, axis=1)
    feature_names: list[str] = list(predictors.columns)
    predictors = np.array(predictors, dtype=np.float32)

    y: DataFrame = data[y_col]
    y = np.array(y, dtype=np.float32)

    viz = dtreeviz(model,
                    predictors,
                    y,
                    target_name="Heart disease",
                    feature_names=feature_names)

    return viz


if __name__ == "__main__":

    pass

    # train,test = get_train_test_datasets("heart.csv")
    # model: DecisionTreeClassifier = get_tree_decision_model(train)
    # get_confusion_matrix(model,train, values="relative")
    # decision_tree = plot_decision_tree(model,train)
    # decision_tree.view()

