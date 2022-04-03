import numpy as np
from sklearn.model_selection import KFold


def test_smoke():
    print("fire?")


def test_kfcv():
    StartedData = np.arange(10, 110, 10)
    print(StartedData)

    kfold = KFold(
        n_splits=5,
        shuffle=True,
        random_state=1
    )

    for TrainData, TestData in kfold.split(StartedData):
        print("Train Data :", StartedData[TrainData], "Test Data :", StartedData[TestData])
